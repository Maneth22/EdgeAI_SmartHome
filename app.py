from flask import Flask, Response, Request, render_template, jsonify
from Devices import Temperature
import time
#from Devices import LightRelay
from gpiozero import LED
import gpiozero
from gpiozero.pins.mock import MockFactory
import threading
from gpiozero import MotionSensor
import time
import requests
from ultralytics import YOLO
import cv2
import board
import AllSensors
import os
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
#os.environ['GPIOZERO_PIN_FACTORY'] = os.environ.get('GPIOZERO_PIN_FACTORY', 'mock')

temperature_values = []
Current_values = []
i2c = busio.I2C(board.SCL, board.SDA)
led = LED(10)
app = Flask(__name__)


def Temperature_loop():
    i = 0
    while True:

        time.sleep(1)
        for value in Temperature.get_Temp():
            temperature_values.append(value)
            print(value)
            # thread_2= threading.Thread(target=update_value_placeholder, args=(value,))
            # thread_2.start()
            # thread_2.join()
            # yield value
            time.sleep(1)


def motionSense():
    i = 0
    pir = MotionSensor(17)
    while True:
        time.sleep(1)
        i += 1
        print("working")
        num_people = 0
        # LED.off()
        # while True:
        pir.wait_for_motion()
        num_people = AllSensors.detection()
        while num_people > 0:
            led.on()
            num_people = AllSensors.detection()
        print(num_people)
        # time.sleep(1)
        # LED.on()
        print("motion detected")
        pir.wait_for_no_motion()
        led.off()
        # time.sleep(1)
        print("motion not detected")
        # LED.off()


def start_motion_sense():
    motionThread = threading.Thread(target=motionSense)
    motionThread.start()

def start_temperature_record():
    tempThread = threading.Thread(target=Temperature_loop)
    tempThread.start()
@app.route("/")
def home():
    start_motion_sense()
    start_temperature_record()
    start_current_record()
    outPut_dic={"Temperature":temperature_values,
                "Current":Current_values}
    return jsonify(outPut_dic)
    
@app.route("/dashboard")
def dashboard():
    start_temperature_record()
    return jsonify({"temperature_values": temperature_values})

@app.route('/send_data', methods=['GET'])
def send_data():
    #data = {'message': 'Hello from Flask!'}
    # Assuming your Streamlit app is running on http://localhost:8501
    streamlit_url = 'http://localhost:8501'
    outPut_dic={"Temperature":temperature_values,
                "Current":Current_values}
    requests.post(streamlit_url, json=outPut_dic)
    return jsonify(outPut_dic)


if __name__ == '__main__':
    app.run()
