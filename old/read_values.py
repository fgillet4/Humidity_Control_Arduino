import serial
import json

ser = serial.Serial('/dev/ttyACM0', 9600)

try:
    while True:
        data = ser.readline().decode('utf-8').strip()
        print(f"Raw Data: {data}")
        try:
            parsed_data = json.loads(data)
            print(parsed_data)
        except json.JSONDecodeError:
            print("Error: Invalid JSON")
except KeyboardInterrupt:
    ser.close()