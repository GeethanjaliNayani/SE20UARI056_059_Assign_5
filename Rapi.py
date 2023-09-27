#Imporing required libraries
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:  #If temp and humidity exists
        print("Temp = {0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))    #then the values will be returned
    else:
        print("Sensor failure. check wiring.");
    time.sleep(3) #sensor sleeps for 3 secs, data will not be recoreded for those 3 secs