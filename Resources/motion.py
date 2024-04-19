from gpiozero import MotionSensor
import time
from gpiozero import LED

pir = MotionSensor(17)
#LED.off()
while True:
    pir.wait_for_motion()
    # time.sleep(1)
    #LED.on()
    print("motion detected")
    pir.wait_for_no_motion()
    # time.sleep(1)
    print("motion not detected")
    #LED.off()
