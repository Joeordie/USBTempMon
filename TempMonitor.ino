#include <DHT.h>
#define DHTPIN 4
#define DHTTYPE DHT11 //dht11

DHT dht(DHTPIN, DHTTYPE);

//counter set up and Test proceedures.

int counter = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  //pinMode(2, INPUT);
  dht.begin();
}

void loop() {
  //counter will normally be < 30
  if (counter < 30) {
    //this counter flashes the LED so we can see that the sketch is running
    digitalWrite(13, HIGH);
    delay(1000);
    digitalWrite(13, LOW);
    delay(1000);
    //counter increments for 1 minute (1 sec + 1 sec * 30 = 60 secs)
    counter++;
  }
  else {
    //once we get to about a minute lets print out the temp.
    int f = dht.readTemperature(true);
    String fForPub = String(f);
      if (fForPub.equals("nan")){
         //do not print it!
      }
      else Serial.println(f);
      
    // reset the counter
    counter = 0;
    
  }

}
