#include <Arduino.h>
#include <U8g2lib.h>
#include <dht.h>

#define outPin 8    // dig pin connected to the DHT sensor


/*
  U8g2lib Example Overview:
    Frame Buffer Examples: clearBuffer/sendBuffer. Fast, but may not work with all Arduino boards because of RAM consumption
    Page Buffer Examples: firstPage/nextPage. Less RAM usage, should work with all Arduino boards.
    U8x8 Text Only Example: No RAM usage, direct communication with display controller. No graphics, 8x8 Text only.
    
*/

// Please UNCOMMENT one of the contructor lines below
// U8g2 Contructor List (Frame Buffer)
// The complete list is available here: https://github.com/olikraus/u8g2/wiki/u8g2setupcpp
// Please update the pin numbers according to your setup. Use U8X8_PIN_NONE if the reset pin is not connected

U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R0, /* clock=*/ SCL, /* data=*/ SDA, /* reset=*/ U8X8_PIN_NONE);   // All Boards without Reset of the Display

// End of constructor list

// ---------------------------------------------------------------------------------------------------------------------

dht DHT; // Create our dht obj

void setup(void) {
  u8g2.begin();
  Serial.begin(9600);
}

void loop(void) {
  // temp sens
  int readData = DHT.read11(outPin);
  float t = DHT.temperature;
  float h = DHT.humidity;
  String temp = String(t);
  String humid = String(h);

  // Print to serial monitor
  Serial.print(F("Temperature (Celcius) = "));
  Serial.print(t);
  Serial.println(F(""));
  Serial.print(F("Humidity = "));
  Serial.print(h);
  Serial.print(F("%"));
  Serial.println(F(""));

  // Render to display
  u8g2.clearBuffer();         // clear the internal memory
  u8g2.setFont(u8g2_font_smart_patrol_nbp_tf);
  u8g2.setCursor(0, 15);
  u8g2.print("Temp (C): " + temp + char(176) + "C");
  u8g2.setCursor(0, 31);
  u8g2.print("Humid: " + humid + "%");
  //u8g2.drawStr(0,10,"it's off!!");  // write something to the internal memory
  u8g2.sendBuffer();          // transfer internal memory to the display
  delay(2000);
}