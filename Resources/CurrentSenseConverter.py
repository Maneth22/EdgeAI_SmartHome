import time
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Create an I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create an ADS1015 ADC instance
ads = ADS.ADS1015(i2c)

# Set the gain (adjust as needed)
GAIN = 3

# Create an analog input channel
current_chan = AnalogIn(ads, ADS.P2)  # Connect ACS712 output to A0

from gpiozero import LED
switch = LED(10)
#switch.on()
print(switch.is_active)
count =0
try:
    while True:
        # Read current
        current = current_chan.voltage / 0.185  # ACS712 sensitivity

        print(f"Current: {current:.2f} A")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nMeasurement stopped by user.")







































"""import board
import busio
from adafruit_ads1x15 import ads1015, ads1115
from adafruit_ads1x15.analog_in import AnalogIn
import time

i2c = busio.I2C(board.SCL, board.SDA)
# i2c = busio.I2C(board.GPIO3, board.GPIO2)
#adc = ADS1015()
ads = ads1015.ADS1015(i2c)
chan = AnalogIn(ads,ads1015.P3)

while True:
    time.sleep(1)
    print(chan.value)
    print(chan.voltage)
    
    """
 
# while True:
#     # channel 0 - channel 1
#     print(adc[(0,1)].value, adc[(0,1)].volts)