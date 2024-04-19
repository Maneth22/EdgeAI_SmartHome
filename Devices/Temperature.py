import time
import board
import adafruit_dht


def get_Temp():
    dhtDevice = adafruit_dht.DHT11(board.D27)

    while True:
        try:
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            Output = "Temp: {:.1f} C    Humidity: {}% ".format(
                    temperature_c, humidity
                )
            #print(Output)

            
    #pip install adafruit-circuitpython-adafruitio
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
        yield Output
        
for val in get_Temp():
    print(val)
    time.sleep(1)
# Initial the dht device, with data pin connected to:
