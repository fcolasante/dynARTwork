#include "GridEYE.h"
#include <stdlib.h>
#include "periph_conf.h"
#include "periph/i2c.h"
#define UNUSED(x) (void)(x)
float GridEYE_getPixelTemperature(unsigned char pixelAddr)
{

  // Temperature registers are numbered 128-255
  // Each pixel has a lower and higher register
  unsigned char pixelLowRegister = TEMPERATURE_REGISTER_START + (2 * pixelAddr);
  int16_t temperature = getRegister(pixelLowRegister, 2);

  // temperature is reported as 12-bit twos complement
  // check if temperature is negative
  if(temperature & (1 << 11))
  {
    // if temperature is negative, mask out the sign byte and 
    // make the float negative
    temperature &= ~(1 << 11);
    temperature = temperature * -1;
  }

  float DegreesC = temperature * 0.25;

  return DegreesC;

}


int16_t getRegister(unsigned char reg, int8_t len)
{
  i2c_t dev = I2C_DEV(0);
  i2c_acquire(dev);
  int16_t result = 0;
  uint8_t data[2];
  uint8_t retval; 

      // Get bytes from sensor
      
      retval = i2c_read_regs(dev, 0x68, reg, data,2, I2C_NOSTOP);
      uint8_t lsb = data[0]; 
      uint8_t msb = data[1];
      printf("retval %d\n", retval);  
      // concat bytes into int
      result = (uint16_t)msb << 8 | lsb;
    UNUSED(retval);
    i2c_release(dev);
    return result;
}