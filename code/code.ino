//#include <AccelStepper.h>
//
//#define X_STEP_PIN         36
//#define X_DIR_PIN          34
//#define X_ENABLE_PIN       30
//#define X_CS_PIN           44
//
//#define Y_STEP_PIN 60
//#define Y_DIR_PIN 61
//#define Y_ENABLE_PIN 56
//#define Y_MIN_PIN 14
//#define Y_MAX_PIN 15
//
//
//#define E0_STEP_PIN 26
//#define E0_DIR_PIN 28
//#define E0_ENABLE_PIN 24
//
//#define E1_STEP_PIN        36
//#define E1_DIR_PIN         34
//#define E1_ENABLE_PIN      30
//#define E1_CS_PIN          44
//
//#define Z_STEP_PIN 46
//#define Z_DIR_PIN 48
//#define Z_ENABLE_PIN 62
//int b;
//AccelStepper stepper1(1, Y_STEP_PIN, Y_DIR_PIN);
//AccelStepper stepper2(1, E0_STEP_PIN, E0_DIR_PIN);
//AccelStepper stepper3(1, Z_STEP_PIN, Z_DIR_PIN);
//AccelStepper stepper4(1, E1_STEP_PIN, E1_DIR_PIN);
//AccelStepper stepper5(1, X_STEP_PIN, X_DIR_PIN);

int steps = 0;
int moveNum = 0;
void setup()
{
//  pinMode(X_ENABLE_PIN , OUTPUT);
//  pinMode(X_DIR_PIN, OUTPUT);
//  pinMode(Y_ENABLE_PIN , OUTPUT);
//  pinMode(Y_DIR_PIN, OUTPUT);
//  pinMode(Z_ENABLE_PIN , OUTPUT);
//  pinMode(Z_DIR_PIN, OUTPUT);
//  pinMode(E0_ENABLE_PIN , OUTPUT);
//  pinMode(E0_DIR_PIN, OUTPUT);
//  pinMode(E1_ENABLE_PIN , OUTPUT);
//  pinMode(E1_DIR_PIN, OUTPUT);
//  digitalWrite(Y_ENABLE_PIN , LOW);
//  digitalWrite(Y_DIR_PIN, LOW);
//  digitalWrite(Z_ENABLE_PIN , LOW);
//  digitalWrite(Z_DIR_PIN, LOW);
//  digitalWrite(E0_ENABLE_PIN , LOW);
//  digitalWrite(E0_DIR_PIN, LOW);
//  digitalWrite(E1_ENABLE_PIN , LOW);
//  digitalWrite(E1_DIR_PIN, LOW);
//  Serial.begin(115200); // use the same baud-rate as the python side
//  stepper1.setMaxSpeed(1250);
//  stepper1.setAcceleration(2000);
//  stepper2.setMaxSpeed(1250);
//  stepper2.setAcceleration(2000);
//  stepper3.setMaxSpeed(1250);
//  stepper3.setAcceleration(2000);
//  stepper4.setMaxSpeed(1250);
//  stepper4.setAcceleration(2000);
//  stepper5.setMaxSpeed(1250);
//  stepper5.setAcceleration(2000);
}

void loop()
{
//  while (Serial.available() > 0 ) {
//    b = Serial.read();
//    Serial.print("I received ");
//    Serial.println(b);
//  }
//  if (b == 48) {
//    if (stepper1.distanceToGo() == 0) {
//      stepper1.moveTo(-40);
//    }
//    if (stepper2.distanceToGo() == 0) {
//      stepper2.moveTo(-40);
//    }
//    if (stepper3.distanceToGo() == 0) {
//      stepper3.moveTo(-40);
//    }
//    if (stepper4.distanceToGo() == 0) {
//      stepper4.moveTo(-40);
//    }
//    if (stepper5.distanceToGo() == 0) {
//      stepper5.moveTo(-40);
//    }
//  }
//  if (b == 49) {
//    if (stepper1.distanceToGo() == 0) {
//      stepper1.moveTo(40);
//    }
//    if (stepper2.distanceToGo() == 0) {
//      stepper2.moveTo(40);
//    }
//    if (stepper3.distanceToGo() == 0) {
//      stepper3.moveTo(40);
//    }
//     if (stepper4.distanceToGo() == 0) {
//      stepper4.moveTo(40);
//    }
//    if (stepper5.distanceToGo() == 0) {
//      stepper5.moveTo(40);
//    }
//  }
//  Serial.flush();
//  stepper1.run();
//  stepper2.run();
}
