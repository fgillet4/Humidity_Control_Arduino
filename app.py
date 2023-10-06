from flask import Flask, render_template, jsonify
import serial
import json
import threading

app = Flask(__name__)
sensor_data = {}

def read_serial():
    global sensor_data
    ser = serial.Serial('/dev/ttyACM0', 9600)
    while True:
        if ser.in_waiting > 0:
            try:
                sensor_data = json.loads(ser.readline().decode('utf-8').strip())
            except Exception as e:
                print(f"Error: {str(e)}")

@app.route("/")
def home():
    return render_template("index.html", data=sensor_data)

@app.route("/data")
def data():
    return jsonify(sensor_data)

if __name__ == "__main__":
    t1 = threading.Thread(target=read_serial)
    t1.start()
    app.run(host='0.0.0.0', port=80)
