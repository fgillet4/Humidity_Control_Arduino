#include <DHT.h>
#include <ArduinoJson.h>
#include <math.h>
/*
   200mA Arduino Uno Max Amperage
   (6 units = 6*2.5mA = 18mA
   3 to 5V power and I/O
   2.5mA max current use during conversion (while requesting data)
   Good for 20-80% humidity readings with 5% accuracy
   Good for 0-50°C temperature readings ±2°C accuracy
   No more than 1 Hz sampling rate (once every second)
   Body size 15.5mm x 12mm x 5.5mm
   4 pins with 0.1" spacing
*/
#define DHTTYPE DHT11 

#define DHTPIN_7 7 //top left
#define DHTPIN_6 6 //top right
#define DHTPIN_5 5 // bottom left
#define DHTPIN_4 4 // bottom right
#define DHTPIN_3 3 // outside 
#define DHTPIN_2 2 // inside

DHT dhts[] = {
  DHT(DHTPIN_7, DHTTYPE),
  DHT(DHTPIN_6, DHTTYPE),
  DHT(DHTPIN_5, DHTTYPE),
  DHT(DHTPIN_4, DHTTYPE),
  DHT(DHTPIN_3, DHTTYPE),
  DHT(DHTPIN_2, DHTTYPE)
};

String DHT_NAMES[6] = {"Top Left", "Top Right", "Bottom Left", "Bottom Right", "Inside", "Outside"};

void setup() {
  Serial.begin(9600);
  for(int i = 0; i < 6; i++) {
    dhts[i].begin();
  }
}

void loop() {
  DynamicJsonDocument doc(1024);

  for(int i = 0; i < 6; i++){
    JsonObject sensor = doc.createNestedObject(DHT_NAMES[i]);

    float relative_humidity = dhts[i].readHumidity();
    float temperature_dry = dhts[i].readTemperature();
      
    if (isnan(relative_humidity)
       || isnan(temperature_dry)) {
      sensor["Error"] = "Failed to read from DHT sensor!";
      continue;
    }
    
    sensor["Temperature C"] = temperature_dry;
    sensor["Relative Humidity %"] = relative_humidity;
  }

  serializeJson(doc, Serial);
  Serial.println();

  delay(2000); // Wait a few seconds between measurements
}
