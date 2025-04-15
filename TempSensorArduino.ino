#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

#define DATA_PIN 15       // Sensor pin
#define BOOT_BUTTON 0    // Data collection button
#define RESET_BUTTON 3   // Reset button

BLEServer *pServer;
BLEService *pService;
BLECharacteristic *pCharacteristic;
bool deviceConnected = false;

// BLE UUIDs (generate your own if needed)
#define SERVICE_UUID        "4fafc201-1fb5-459e-8fcc-c5c9c331914b"
#define CHARACTERISTIC_UUID "beb5483e-36e1-4688-b7f5-ea07361b26a8"

// Callback for BLE connection events
class MyServerCallbacks : public BLEServerCallbacks {
    void onConnect(BLEServer* pServer) {
      deviceConnected = true;
      Serial.println("BLE Client Connected!");
    }
    void onDisconnect(BLEServer* pServer) {
      deviceConnected = false;
      Serial.println("BLE Client Disconnected!");
      // Restart advertising to allow reconnection
      pServer->startAdvertising();
    }
};

void setup() {
  Serial.begin(115200);
  pinMode(DATA_PIN, INPUT);
  pinMode(BOOT_BUTTON, INPUT_PULLUP);
  pinMode(RESET_BUTTON, INPUT_PULLUP);

  // Initialize BLE
  BLEDevice::init("ESP32_Sensor_Device"); // Name your device
  pServer = BLEDevice::createServer();
  pServer->setCallbacks(new MyServerCallbacks());

  // Create a BLE Service
  pService = pServer->createService(SERVICE_UUID);

  // Create a BLE Characteristic for sensor data
  pCharacteristic = pService->createCharacteristic(
                      CHARACTERISTIC_UUID,
                      BLECharacteristic::PROPERTY_READ |
                      BLECharacteristic::PROPERTY_NOTIFY
                    );
  pCharacteristic->addDescriptor(new BLE2902());

  // Start the service
  pService->start();

  // Start advertising (makes device discoverable)
  pServer->getAdvertising()->start();
  Serial.println("BLE Server Started. Waiting for client...");
}

void loop() {
  // Check if BOOT button is pressed (send sensor data)
  if (digitalRead(BOOT_BUTTON) == LOW) {
    int sensorValue = analogRead(DATA_PIN);
    Serial.print("Sensor Value: ");
    Serial.println(sensorValue);

    // Send data via BLE if connected
    if (deviceConnected) {
      char buffer[10];
      sprintf(buffer, "%d", sensorValue);
      pCharacteristic->setValue(buffer);
      pCharacteristic->notify();  // Send notification to client
      Serial.println("Sent data over BLE!");
    }
    delay(200);  // Debounce
  }

  // Check if RESET button is pressed (reboot)
  if (digitalRead(RESET_BUTTON) == LOW) {
    Serial.println("Reset button pressed - restarting...");
    delay(100);
    ESP.restart();
    delay(200);
  }
}
