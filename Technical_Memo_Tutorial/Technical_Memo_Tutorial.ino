//Variable Declartion
const int m1 = 4, m2 = 5, m3 = 6, m4 = 7; // Motor Pins Declartion
int step_number = 0;  //step counter
const int button = 8; //push button pin
int buttonState;  //check the button state
int lastPress = LOW;  //see if it was pressed
unsigned long lastDebounceTime = 0;  //for debouncing calculation
unsigned long debounceDelay = 100;  //gap to ignore button press
bool spinOfMotorDirection = false; //false for counter clockwise, true for clockwise
const int MotorSpinTime = 2500;  //run motor for a certain amount of time
unsigned long previousMillis = 0; //for debouncing
unsigned long activeMotorTime = 0; //check when the motor spin began
bool wasButtonPressed = false; //boolean to check if a function return


void setup() {
   Serial.begin(19200);
   pinMode(m1, OUTPUT);
   pinMode(m2, OUTPUT);
   pinMode(m3, OUTPUT);
   pinMode(m4, OUTPUT);
   pinMode(button, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  bool wasPressed = listenForButton();
  ///Serial.println("Comms Ready");
  if(wasPressed){
    if ((millis() - activeMotorTime) < MotorSpinTime){
      actuateMotor(spinOfMotorDirection);
      delay(2);
      }
    if (millis() - activeMotorTime >= MotorSpinTime){
      stopMotor();
    }
  }
}

boolean listenForButton(){
  int listening = digitalRead(button);  // 
  //see for a diffrent button state than last time
  if (listening != lastPress){
    lastDebounceTime = millis();   //setup a timer
  }
  //check to see if the last button state change timing was longer than the delay we set
  if ((millis() - lastDebounceTime) > debounceDelay) {
      //check if the button state is different
      if (listening != buttonState){
        buttonState = listening;
        //we start the timer if button state is high
        if (buttonState == HIGH){
          Serial.println(buttonState);
          spinOfMotorDirection = !spinOfMotorDirection; //will change the durection
          activeMotorTime = millis(); //start the motor timer
          wasButtonPressed = true; //update a variable so we can run the motor in the loop function
          }
      }
  }
  Serial.println(buttonState);
}

//stop the motor movement
void stopMotor(){
  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);
  digitalWrite(m3, LOW);
  digitalWrite(m4, LOW);
}

//spin the motor
void actuateMotor(bool rotateDirection){
  //Serial.println("moving motor");
    if(rotateDirection){
switch(step_number){
  case 0:
  digitalWrite(m1, HIGH);
  digitalWrite(m2, LOW);
  digitalWrite(m3, LOW);
  digitalWrite(m4, LOW);
  break;
  case 1:
  digitalWrite(m1, LOW);
  digitalWrite(m2, HIGH);
  digitalWrite(m3, LOW);
  digitalWrite(m4, LOW);
  break;
  case 2:
  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);
  digitalWrite(m3, HIGH);
  digitalWrite(m4, LOW);
  break;
  case 3:
  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);
  digitalWrite(m3, LOW);
  digitalWrite(m4, HIGH);
  break;
} 
  }else{
    switch(step_number){
  case 0:
  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);
  digitalWrite(m3, LOW);
  digitalWrite(m4, HIGH);
  break;
  case 1:
  digitalWrite(m1, LOW);
  digitalWrite(m2, LOW);
  digitalWrite(m3, HIGH);
  digitalWrite(m4, LOW);
  break;
  case 2:
  digitalWrite(m1, LOW);
  digitalWrite(m2, HIGH);
  digitalWrite(m3, LOW);
  digitalWrite(m4, LOW);
  break;
  case 3:
  digitalWrite(m1, HIGH);
  digitalWrite(m2, LOW);
  digitalWrite(m3, LOW);
  digitalWrite(m4, LOW);
} 
  }
step_number++;
  if(step_number > 3){
    step_number = 0;
  }
}
