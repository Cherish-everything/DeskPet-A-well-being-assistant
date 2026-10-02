# DeskPet: Hydration Tracker & Room Comfort Monitor

An automated desktop companion built with Arduino and Python to keep your workspace comfortable and maintain healthy daily hydration habits:)

The DeskPet monitors ambient temperature and humidity, alerts you when your room needs ventilation, reminds you to drink water every hour, and logs your daily water intake to a organized JSON file upon button presses.

---

## Key Features

* **One-Click Water Logging:** Press the desktop button to instantly log 400 mL of water intake.
* **Hourly Reminders:** Automatically plays an audible chime every hour to remind you to hydrate. Logging water resets the timer.
* **Smart Environmental Monitor:** Uses a DHT11 and IR proximity sensor to check room comfort only when you are sitting at your desk 30C temperature and 60% humidity trigger an "Open a window!" alert).
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
```

### Bill of Materials (BOM)

| Category | Item | Description / Spec | Qty | Footprint / Connection | Target Vendor / Search Link | Est. Unit Price (USD) | Est. Total Price (USD) |
| :--- | :--- | :--- | :---: | :--- | :--- | :---: | :---: |
| **Core Hardware** | **Microcontroller** | Arduino Uno R3 Board | 1 | Standalone Board | [Arduino Uno R3](https://www.amazon.com/dp/B008GRTSV6) | $6.00 | $6.00 |
| **Core Hardware** | **USB Cable** | USB Type-A to Type-B Cable | 1 | Standard USB | [USB Cable](https://www.amazon.com/dp/B00NH11KIK) | $1.50 | $1.50 |
| **On-Board PCB** | **Custom PCB** | DeskPet Custom PCB Shield (2-layer FR-4) | 1 | Custom Shield | [JLCPCB Order](https://jlcpcb.com) | $1.50 | $1.50 |
| **On-Board PCB** | **Push Button** | 6x6mm Through-Hole Tactile Switch | 1 | `SW_PUSH_6mm` | [LCSC Tactile Switch](https://www.lcsc.com/product-detail/C128634.html) | $0.15 | $0.15 |
| **On-Board PCB** | **Buzzer** | 12mm Passive Piezo Buzzer | 1 | `BUZZER-PTH` | [LCSC Piezo Buzzer](https://www.lcsc.com/product-detail/C96436.html) | $0.35 | $0.35 |
| **On-Board PCB** | **Resistor (Optional)** | 10k Ohm 1/4W Through-Hole Resistor | 1 | Axial-0.3 | [LCSC 10k Resistor](https://www.lcsc.com/product-detail/C58620.html) | $0.04 | $0.04 |
| **On-Board PCB** | **Capacitor (Optional)** | 0.1uF Ceramic Capacitor | 1 | Radial / 2.54mm pitch | [LCSC 0.1uF Cap](https://www.lcsc.com/product-detail/C14022.html) | $0.04 | $0.04 |
| **Off-Board / Modules** | **DHT11 Sensor** | DHT11 Temp & Humidity Module | 1 | 3-Pin Connector | [Amazon DHT11 Module](https://www.amazon.com/dp/B01DKC2GQ0) | $1.20 | $1.20 |
| **Off-Board / Modules** | **IR Proximity Sensor** | Active-LOW IR Obstacle Sensor Module | 1 | 3-Pin Connector | [Amazon IR Sensor](https://www.amazon.com/dp/B073S1SNNW) | $0.80 | $0.80 |
| **Off-Board / Modules** | **Sensor Pin Headers** | 1x3 Male Pin Headers (2.54mm pitch) | 2 | `Conn_01x03_Pin` | [LCSC 1x3 Headers](https://www.lcsc.com/product-detail/C2893.html) | $0.08 | $0.16 |
| **Off-Board / Modules** | **Shield Headers** | 2.54mm Male Pin Header Strip | 1 | Standard Arduino Pins | [LCSC Male Headers](https://www.lcsc.com/product-detail/C2891.html) | $0.35 | $0.35 |
| **Off-Board / Modules** | **Jumper Wires** | Female-to-Female Jumper Wires | 1 set | DuPont 2.54mm | [Amazon DuPont Wires](https://www.amazon.com/dp/B00KG3KNOE) | $0.80 | $0.80 |
| **Enclosure & Hardware** | **Enclosure Body & Lid** | 3D-Printed Custom Shell (PLA/PETG) | 1 | Custom 3D Model | [Polymaker Filament](https://www.polymaker.com) | $1.50 | $1.50 |
| **Enclosure & Hardware** | **Fasteners** | M3 x 8mm Button/Cap Head Screws | 4 | M3 Thread | [Amazon M3 Screws](https://www.amazon.com/dp/B013S3W3E4) | $0.05 | $0.20 |
| **Enclosure & Hardware** | **Threaded Inserts** | M3 Brass Heat-Set Inserts (M3 x 5 x 4 mm) | 4 | M3 x 5 mm Boss | [Amazon Heat-Set Inserts](https://www.amazon.com/dp/B08T17223P) | $0.08 | $0.32 |
