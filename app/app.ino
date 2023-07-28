#include <Wire.h>

#include "EmonLib.h"

//#define VOLT_CAL 592
#define VOLT_CAL 500

EnergyMonitor emon1;
int relay1Blue = 10;
int relay2Orange = 9;
int relay3Vert = 8;
int voltageReel = 7;
String text;
int val1;
int val2;

void setup() {
  Serial.begin(9600);
  pinMode(relay1Blue, OUTPUT);
  pinMode(relay2Orange, OUTPUT);
  pinMode(relay3Vert, OUTPUT);
  pinMode(voltageReel, OUTPUT);
  digitalWrite(relay1Blue, LOW);
  digitalWrite(relay2Orange, LOW);
  digitalWrite(relay3Vert, LOW);
  digitalWrite(voltageReel, !LOW);
  emon1.voltage(1, VOLT_CAL, 1.7);  // Voltage: input pin, calibration, phase_shift
}

void loop() {
  emon1.calcVI(25, 500);  // Calculate all. No.of half wavelengths (crossings), time-out

  val1 = analogRead(A0);
  float temps;
  temps= val1/4.092;
  val1 = (int)temps;
  val2 = ((val1 % 100)/10);
  //Serial.println(val2);

  float supplyVoltage = emon1.Vrms;
  if (supplyVoltage >= 100) {
  digitalWrite(relay1Blue, !LOW);
  digitalWrite(relay2Orange,! LOW);
  digitalWrite(relay3Vert, !LOW);
  } else {
  digitalWrite(relay1Blue, LOW);
  digitalWrite(relay2Orange, LOW);
  digitalWrite(relay3Vert, LOW);
  }

  Serial.println(supplyVoltage);
}
