#define DATA_PIN 15  // Use D15 for data input  

void setup() {  
  Serial.begin(115200);          // Initialize Serial for output  
  pinMode(DATA_PIN, INPUT);      // Set DATA_PIN as input  
}  

void loop() {  
  int sensorValue = analogRead(DATA_PIN);  // Read the analog value from the CNT5 sensor  
  Serial.print("Sensor Value: ");  
  Serial.println(sensorValue);               // Print the sensor value (0 to 4095 for a 12-bit ADC)  

  delay(1000);  // Delay for 1 second before the next read  
}  