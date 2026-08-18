# DeskPet: Hydration Tracker & Room Comfort Monitor

An automated desktop companion built with Arduino and Python to keep your workspace comfortable and maintain healthy daily hydration habits:)

The DeskPet monitors ambient temperature and humidity, alerts you when your room needs ventilation, reminds you to drink water every hour, and logs your daily water intake to a organized JSON file upon button presses.

---

## Key Features

* **One-Click Water Logging:** Press the desktop button to instantly log 400 mL of water intake.
* **Hourly Reminders:** Automatically plays an audible chime every hour to remind you to hydrate. Logging water resets the timer.
* **Smart Environmental Monitor:** Uses a DHT11 and IR proximity sensor to check room comfort only when you are sitting at your desk ($\ge 30^\circ\text{C}$ temperature and $\ge 60\%$ humidity trigger an "Open a window!" alert).
* **Categorized JSON Analytics:** Python backend aggregates water logs by date (`YYYY-MM-DD`) while maintaining lifetime totals.

---

## Hardware Requirements

* **Microcontroller:** Arduino Uno
* **Sensors:**
  * DHT11 Temperature & Humidity Sensor
  * IR Proximity Sensor (Active-LOW)
* **Outputs & Controls:**
  * Push Button (INPUT_PULLUP)
  * Passive Buzzer
  * Jumper Wires & Breadboard

### Pin Connections

| Component | Arduino Pin |
| :--- | :--- |
| **IR Proximity Sensor** | Pin 2 |
| **DHT11 Data** | Pin 3 |
| **Buzzer (+)** | Pin 5 |
| **Push Button** | Pin 9 |

---

## 📂 Project Structure

```text
DeskPet/
├── main.cpp          # Arduino code handling sensor timing, alerts, and serial output
├── logger.py          # Python script receiving serial data and writing to JSON
└── water_log.json     # Generated database tracking daily and lifetime water intake
