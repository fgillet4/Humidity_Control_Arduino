from flask import Flask, render_template, jsonify
import serial
import json
import threading

app = Flask(__name__)

latest_data = {}

def read_serial():
    global latest_data
    ser = serial.Serial('/dev/ttyACM0', 9600)
    while True:
        try:
            data = ser.readline().decode('utf-8').strip()
            latest_data = json.loads(data)
        except (json.JSONDecodeError, serial.SerialException):
            continue

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/latest_data')
def get_latest_data():
    return jsonify(latest_data)

if __name__ == "__main__":
    t1 = threading.Thread(target=read_serial)
    t1.start()
    app.run(host='0.0.0.0', port=80, threaded=True)
