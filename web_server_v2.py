from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import serial
import json
import threading

app = Flask(__name__)

# SQLite setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class DataPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String, nullable=False)

latest_data = {}

def read_serial():
    global latest_data
    ser = serial.Serial('/dev/ttyACM0', 9600)
    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
            latest_data = json.loads(data)
            
            # Save to the database
            data_point = DataPoint(data=data)
            db.session.add(data_point)
            db.session.commit()
        except (json.JSONDecodeError, serial.SerialException):
            continue

@app.route('/')
def home():
    return render_template('index_v2.html')

@app.route('/latest_data')
def get_latest_data():
    return jsonify(latest_data)

@app.route('/historical_data')
def get_historical_data():
    # Fetch the last 100 data points, for example
    data_points = DataPoint.query.order_by(DataPoint.id.desc()).limit(100).all()
    return jsonify([json.loads(dp.data) for dp in data_points])

@app.route('/control_relay', methods=['POST'])
def control_relay():
    state = request.json['state']
    # Control your relay here based on the 'state'
    # For this, you might need GPIO libraries or similar to interact with the relay.
    return jsonify(status="success")

@app.route('/set_pid', methods=['POST'])
def set_pid():
    set_point = request.json['set_point']
    # Implement your PID set point logic here.
    return jsonify(status="success")
@app.route('/update_pid', methods=['POST'])
def update_pid():
    try:
        data = request.json
        kp = data['kp']
        ki = data['ki']
        kd = data['kd']
        
        # Send these values to your Arduino or process them as needed.
        # Example: ser.write(f"SET_PID,{kp},{ki},{kd}\n".encode('utf-8'))

        return "PID values updated successfully", 200
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # This will create the SQLite database file if it doesn't exist
    t1 = threading.Thread(target=read_serial)
    t1.start()
    app.run(host='0.0.0.0', port=80, threaded=True)
