/*
 * PIR sensor code
 * by Joseph Maina
 */
 String data = "Motion detected!";
 
int ledPin = 13;                // choose the pin for the LED
int inputPin = 5;               // this is the input pin for the first PIR sensor
int inputPinTwo = 7;            //this is the input pin for the second PIR sensor
int pirState = LOW;             // for both sensors, we start by assuming no motion detected
int pirTwoState = LOW;         
int val = 0;                    // this variable and the one below it are there to read the pin status
int val2 = 0;
 
void setup() {
  
  pinMode(ledPin, OUTPUT);      // declare LED as output (there is one on the board that is installed; in any case one can manually attach an LED to pin 13)
  pinMode(inputPin, INPUT);     // declare sensors as input (this one and the one below it)
  pinMode(inputPinTwo, INPUT);
 
  Serial.begin(9600); //baudrate
}
 
void loop(){
  val = digitalRead(inputPin);  // read input values from the first and second sensor
  val2 = digitalRead(inputPinTwo);
  if ((val == HIGH) && (val2 == HIGH)) {            // check if the input is HIGH
    digitalWrite(ledPin, HIGH);                     // turn LED ON
    if ((pirState == LOW) && (pirTwoState == LOW)) {
      // we have just turned on
      Serial.println(data);
      // We only want to print on the output change, not state
      pirState = HIGH;
      pirTwoState = HIGH;
    }
  } else {
    digitalWrite(ledPin, LOW); // turn LED OFF
    if ((pirState == HIGH) && (pirTwoState == HIGH)){
      // we have just turned off
      Serial.println("Motion ended!");
      // We only want to print on the output change, not state
      pirState = LOW;
      pirTwoState = LOW;
    }
  }
}
