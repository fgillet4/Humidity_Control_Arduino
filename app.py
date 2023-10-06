from flask import Flask, render_template, jsonify
import serial
import json
import threading
import time

app = Flask(__name__)
sensor_data = {}

def read_serial():
    global sensor_data
    while True:
        try:
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            line = ser.readline().decode('utf-8').strip()
            if line:
                sensor_data = json.loads(line)
            ser.close()  # Close the connection after reading
        except json.JSONDecodeError:
            print("Error: Invalid JSON data received.")
        except serial.SerialException as e:
            print(f"Serial connection error: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
        finally:
            time.sleep(1)  # Avoid busy-waiting

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
