//set pin numbers
//const won't change
const int ledPin = 13;   //the number of the LED pin
const int ldrPin = A0;  //the number of the LDR pin
int lightValue = -1;

void setup() {

  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);  //initialize the LED pin as an output
  pinMode(ldrPin, INPUT);   //initialize the LDR pin as an input

  Serial.println("Enter your desired light value?");  // Asking the user for input value
  while (Serial.available() == 0)  
  { //Wait for user input  }  
    lightValue = Serial.parseInt(); // Store the desire value into "lightValue" 
    }
    Serial.println(lightValue); 
  }

void loop() {
  
  int ldrStatus = analogRead(ldrPin);   //read the status of the LDR value

  //5check if the LDR status is <= 300
  //if it is, the LED is HIGH

  if (ldrStatus <= lightValue) {

    digitalWrite(ledPin, HIGH);               //turn LED on
    Serial.println("LED is ON " + String(ldrStatus));
   }
  else {

    digitalWrite(ledPin, LOW);          //turn LED off
    Serial.println("LED is OFF " + String(ldrStatus));
  }
}