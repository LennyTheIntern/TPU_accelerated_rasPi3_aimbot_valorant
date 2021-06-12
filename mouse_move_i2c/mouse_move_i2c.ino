

// Include the Wire library for I2C
#include <Wire.h>
#include <Mouse.h>

void setup()
{
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  
  Mouse.begin();
  Wire.onReceive(receiveEvent);
}

// reads the wire to get the x and y for the mouse move
void receiveEvent(int howMany) 
{
 static bool x_flag = true;
 static int16_t data = 0;
 static int16_t bit_offset = 0;
 static int16_t x;
 static int16_t y;

  while (Wire.available()) { // loop through all but the last
    data |= Wire.read()<< bit_offset; // receive byte as a character
    bit_offset += 8;
  }

  if(bit_offset > 8)
  {
    if(x_flag)
    {
     x = data;
     bit_offset = 0;
     data = 0;
    }
    else
    {
      y = data;
      bit_offset = 0;
      data = 0;
      mouse_move(x,y);
    }
    x_flag = !x_flag;
  }
}


///max move for the mouse funtion is 127, so you have to move along the x and y axis 127 units at a time
void mouse_move(int16_t x, int16_t y )
{
  while( x != 0 && y!= 0 )//
  {
    int temp_x = abs(x) >=  127 ? x:(127 * abs(x)/x);
    int temp_y = abs(y) >= 127 ? y:(127 * abs(y)/y);
    x -= temp_x;
    y -= temp_y;
   Mouse.move(temp_x,temp_x);
  }
}

void loop()
{
}
