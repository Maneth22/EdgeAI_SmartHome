from gpiozero import InputDevice
from gpiozero.pins.lgpio import LGPIOFactory
from time import sleep

# Set the GPIO pin factory
InputDevice.pin_factory = LGPIOFactory(chip=4)

# Set the input pin
INPUT_PIN = 22
device = InputDevice(INPUT_PIN)

# Start the main loop
while True:
    if device.is_active:  # Physically read the pin now
        
        print(device.value)
        
        print('3.3')
    else:
        # print('0')
        print(device.value)
    sleep(1)  # Sleep for a full second before restarting the loop