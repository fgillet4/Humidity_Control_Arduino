from flask import Flask, render_template, jsonify
import serial
import json
import threading
import time

app = Flask(__name__)
sensor_data = {}

def read_serial():
    global sensor_data
    ser = serial.Serial('/dev/ttyACM0', 9600)
    while True:
        if ser.in_waiting > 0:
            raw_data = ser.readline().decode('utf-8').strip()
            print(f"Raw data: {raw_data}")  # Log raw data
            try:
                sensor_data = json.loads(raw_data)
            except Exception as e:
                print(f"Error: {str(e)}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data")
def data():
    return jsonify(sensor_data)

if __name__ == "__main__":
    t1 = threading.Thread(target=read_serial)
    t1.start()
    app.run(host='0.0.0.0', port=80, threaded=True)
