from gpiozero import LED
import gpiozero
from time import sleep
from gpiozero.pins.mock import MockFactory


#led = LED(10)
"""
while True:
    led.on()
    print("on")
    sleep(1)
    led.off()
    print("fuck off")
    sleep(1)"""



def Switch_on(GPIOpin):
    switch = LED(GPIOpin)
    if switch.is_active:
        print("already on")
    else:
        switch.on()
        print("switch "+ str(GPIOpin)+" is switched On")
    sleep(2)


def Switch_0ff(GPIOpin):
    switch = LED(GPIOpin)
    if switch.is_active:
        switch.off()
        print("switch "+ str(GPIOpin)+" is switched Off")
    else:
        print("switch is already off")
    switch.close()

def switch_on_off(GPIOpin):
    switch = LED(GPIOpin)
    if switch.is_active:
        switch.on()
        print("switch "+ str(GPIOpin)+" is switched Off")
        sleep(2)
    else:
        switch.off()
        print("switch is already off")
        sleep(2)
        switch.close()
