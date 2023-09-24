
#include <ESP8266WiFi.h>
#include <NTPClient.h>
#include <WiFiUdp.h>

// Replace with your network credentials
const char *ssid     = "Vicente";
const char *password = "Vicente1";

// Define NTP Client to get time
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org");

//Week Days

void setup() {
  // Initialize Serial Monitor
  pinMode(5,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(0,OUTPUT);
  Serial.begin(115200);

  
  // Connect to Wi-Fi
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

// Initialize a NTPClient to get time
  timeClient.begin();

  timeClient.setTimeOffset(0);
}

void loop() {
  timeClient.update();

   
  int currentsecond = timeClient.getSeconds();
  Serial.print("Seconds: ");
  Serial.println(currentsecond);  
  if(currentsecond>=0 && currentsecond<20){
    digitalWrite(5,HIGH);
    digitalWrite(4,LOW);
    digitalWrite(0,LOW);
  }
  if(currentsecond>=20 && currentsecond<40){
    digitalWrite(5,LOW);
    digitalWrite(4,HIGH);
    digitalWrite(0,LOW);
  }
  if(currentsecond>=40 && currentsecond<60){
    digitalWrite(5,LOW);
    digitalWrite(4,LOW);
    digitalWrite(0,HIGH);
  }



  Serial.println("");

  delay(2000);}