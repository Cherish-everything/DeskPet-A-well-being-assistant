#include <Arduino.h>
#include <DHT.h>

#define IR_PIN 2
#define DHT_PIN 3
#define BUZZER_PIN 5
#define DHT_TYPE DHT11
#define BUTTON_PIN 9

DHT dht(DHT_PIN, DHT_TYPE);

int lastButtonState = HIGH;
unsigned long lastDHTReadTime = 0;
const unsigned long dhtInterval = 2000;

// Water intake reminder timer (1 hour = 3600000 ms)
const unsigned long reminderInterval = 3600000;
unsigned long lastWaterTime = 0;

float temp = 0;
float humidity = 0;

void playReminderBeep()
{
  // Beep twice as a quick reminder sound
  tone(BUZZER_PIN, 880, 150); // A5 note
  delay(200);
  tone(BUZZER_PIN, 1175, 250); // D6 note
  delay(300);
  noTone(BUZZER_PIN);
}

void setup()
{
  Serial.begin(9600);
  pinMode(IR_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  dht.begin();

  lastWaterTime = millis(); // Initialize timer on startup
}

void loop()
{
  unsigned long currentMillis = millis();

  // 1. Button Logic (Resets the reminder timer)
  int currentButtonState = digitalRead(BUTTON_PIN);
  if (lastButtonState == HIGH && currentButtonState == LOW)
  {
    Serial.println("{\"WaterIntake\": 400}");
    lastWaterTime = currentMillis; // Reset 1-hour timer upon drinking
    delay(50);
  }
  lastButtonState = currentButtonState;

  // 2. Hourly Water Reminder Check
  if (currentMillis - lastWaterTime >= reminderInterval)
  {
    playReminderBeep();
    Serial.println("Reminder: Drink some water!");
    // Short grace period before beeping again if ignored (e.g., every 5 minutes)
    lastWaterTime = currentMillis - (reminderInterval - 300000);
  }

  // 3. DHT Sensor Reading
  if (currentMillis - lastDHTReadTime >= dhtInterval)
  {
    lastDHTReadTime = currentMillis;
    temp = dht.readTemperature();
    humidity = dht.readHumidity();
  }

  // 4. Room Comfort Alert Logic
  int personPresent = digitalRead(IR_PIN);
  if (personPresent == LOW && humidity >= 60 && temp >= 30)
  {
    Serial.print("Temperature: ");
    Serial.print(temp);
    Serial.print("°C, Humidity: ");
    Serial.print(humidity);
    Serial.println("% - Open a window!");
    tone(BUZZER_PIN, 1000);
  }
  else if (currentMillis - lastWaterTime < reminderInterval)
  {
    noTone(BUZZER_PIN);
  }

  delay(10);
}