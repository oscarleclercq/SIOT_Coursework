import Adafruit_DHT
 
#sensor type set to DHT11
sensor=Adafruit_DHT.DHT11
 
#set gpio pin the signal pin of the dht11 is connected to
gpio=7
 
#read_retry will retry getting a reading up to 15 times
humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

#function returns the reading to main.py
def get_temp():
    if humidity is not None and temperature is not None:
        return temperature
    else:
        return None
