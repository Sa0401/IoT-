void setup() {
  Serial.begin(9600);
  pinMode(26, INPUT);
}

void loop() {
  int sensorValue = analogRead(26);
  Serial.println(sensorValue);
  delay(1);
}
