import serial
import json
import time
import os
from datetime import datetime

SERIAL_PORT = 'COM3'
BAUD_RATE = 9600

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(SCRIPT_DIR, 'water_log.json')

def init_JSON_file():
    if not os.path.exists(JSON_FILE) or os.path.getsize(JSON_FILE) == 0:
        default_structure = {
            "total_lifetime_ml": 0,
            "daily_summary": {}
        }
        with open(JSON_FILE, 'w') as file:
            json.dump(default_structure, file, indent=4)

def log_water(amount):
    """Update total intake and categorize by day."""
    data = {"total_lifetime_ml": 0, "daily_summary": {}}
    
    if os.path.exists(JSON_FILE) and os.path.getsize(JSON_FILE) > 0:
        with open(JSON_FILE, 'r') as f:
            try:
                loaded = json.load(f)
                if isinstance(loaded, dict) and "daily_summary" in loaded:
                    data = loaded
            except json.JSONDecodeError:
                pass

    now = datetime.now()
    today_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M:%S')

    # Update global total
    data["total_lifetime_ml"] += amount

    # Initialize date category if missing
    if today_str not in data["daily_summary"]:
        data["daily_summary"][today_str] = {
            "daily_total_ml": 0,
            "logs": []
        }

    # Add entry to specific day
    data["daily_summary"][today_str]["daily_total_ml"] += amount
    data["daily_summary"][today_str]["logs"].append({
        "amount_ml": amount,
        "time": time_str
    })

    with open(JSON_FILE, 'w') as f:
        json.dump(data, f, indent=4)
        f.flush()

def main():
    init_JSON_file()
    print(f"Saving logs to: {JSON_FILE}")
    print(f"Connecting to Arduino on {SERIAL_PORT}...")

    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
    time.sleep(2)
    ser.reset_input_buffer()

    print("Listening for events...")
    while True:
        try:
            raw_bytes = ser.readline()
            line = raw_bytes.decode('utf-8', errors='ignore').strip()

            if line.startswith('{') and line.endswith('}'):
                water_data = json.loads(line)
                amount = water_data.get("WaterIntake", 0)
                log_water(amount)
                print(f"[SUCCESS] Added {amount} ml! Logged under date: {datetime.now().strftime('%Y-%m-%d')}")
            elif line:
                print(f"[Arduino]: {line}")

        except json.JSONDecodeError:
            print(f"[Error] Couldn't parse JSON: {line}")
        except KeyboardInterrupt:
            print("\nLogging stopped.")
            ser.close()
            break

if __name__ == "__main__":
    main()