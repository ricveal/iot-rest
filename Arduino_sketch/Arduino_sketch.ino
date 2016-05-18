/* RestClient for sending JSON data sensor
 *
 * This implementation uses Ethernet Shield
 * 
 * by Ricardo Vega (ricveal)
 */

#include <Ethernet.h>
#include <SPI.h>
#include "DHT.h"
#include <ArduinoJson.h>
#include "RestClient.h"

#define DHTPIN 2     // Pin de conexion del sensor
#define DHTTYPE DHT11   // DHT 11 
#define delayTime 300  // Time in seconds beetwen sendings
#define IP "192.168.1.6" // Server IP
#define PORT 5000     // Server Port

DHT dht(DHTPIN, DHTTYPE);
RestClient client = RestClient(IP, PORT);

//Setup
void setup() {
  Serial.begin(9600);
  // Connect via DHCP
  Serial.println("connect to network");
  client.dhcp();
  dht.begin();
/*
  // Can still fall back to manual config:
  byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
  //the IP address for the shield:
  byte ip[] = { 192, 168, 2, 11 };
  Ethernet.begin(mac,ip);
*/
  Serial.println("Setup!");
}

String response;
void loop(){
  float t = dht.readTemperature();
  response = "";
  client.setHeader("Authorization: Basic cmljdmVhbDoxMjM0==");
  client.setHeader("Content-Type: application/json");
  StaticJsonBuffer<200> jsonBuffer;
  char json[256];
  JsonObject& root = jsonBuffer.createObject();
  root["temperature"] = t;
  root.printTo(json, sizeof(json));
  Serial.println(json);
  int statusCode = client.post("/api/v1.0/temperature", json, &response);
  Serial.print("Status code from server: ");
  Serial.println(statusCode);
  Serial.print("Response body from server: ");
  Serial.println(response);
  delay(delayTime*1000);
}
