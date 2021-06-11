/*
  Arduino Slave for Raspberry Pi Master
  i2c_slave_ard.ino
  Connects to Raspberry Pi via I2C
  
  DroneBot Workshop 2019
  https://dronebotworkshop.com
*/
 
// Include the Wire library for I2C
#include <Wire.h>
#include <Mouse.h>
// LED on pin 13
const int ledPin = 13; 
 
void setup() {
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  Mouse.begin();
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);
  Serial.begin(115200);
  // Setup pin 13 as output and turn LED off
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
}
 
// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
 static bool x_flag = true;
 static int16_t c = 0;
 static int16_t count = 0;
 static int16_t x;
 static int16_t y;
  while (Wire.available()) { // loop through all but the last
    c |= Wire.read()<< count; // receive byte as a character
    count += 8;
  }
  if(count > 8)
  {
    if(x_flag)
    {
     x = c;
     count = 0;
     c = 0;
    }
    else
    {
      y = c;
      count = 0;
      c = 0;
      mouse_move(x,y);
    }
    x_flag = !x_flag;
  }     
}

void mouse_move(int16_t x, int16_t y )
{
  //Serial.println(x);
  //Serial.println(y);
  if(x == 0xA0A0)
  {
    Mouse.click();
  }
  else if (x < 2000 && y < 2000 )
  {
  int16_t mouse_x = 0;
  int16_t mouse_y = 0;
  bool yflag = false;
  bool xflag = false;
  while( !yflag || !xflag )//
  {
    if( x > 127)// what if the value is negitive
    {
      mouse_x = 127;
      x -= 127;
    }
    else if( x < -127 )
    {
      mouse_x = -127;
      x += 127;
    }
    else
    {
      mouse_x = x;
      x = 0;
      xflag = true;
    }

    if(y > 127)// what if the value is negitive
    {
      mouse_y = 127;
      y -= 127;
    }
    else if(y < -127 )
    {
      mouse_y = -127;
      y += 127;
    }
    else
    {
      mouse_y = y;
      y = 0;
      yflag = true;
    }
      //Serial.println("x move");
      //Serial.println(mouse_x);
      //Serial.println("y_move");
      //Serial.println(mouse_y);

      Mouse.move(mouse_x,mouse_y);
  }
  }
  //delay(100);
}
void loop() {
}
