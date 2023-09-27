# SE20UARI056_059_Assign_5
## Team Members:
1. Geethanjali Nayani, SE20UARI056
2. Gowravelli Saketh Rao, SE20UARI059
## Assignment-5
## Data Acquisition using Raspberry Pi Report
For the project, we have used DHT11 sensor (digital sensor) for capturing temperature and humidity. It uses a thermistor (for temp) and humidity sensor (for humidity) to measure the surrounding air and then it sends out a digital signal onto the data pin.
For the Raspberry Pi, has about a 40-pin GPIO header, and this header provides 2 of 5V, 2 of 3.3V, 8 ground pins, and a lot of GPIO pins. At the 40 pins GPIO header, we can connect an extension cable and a breadboard where we can put our final sensor.
Then we connected this DHT11 sensor with our Raspberry Pi to capture the temperature and humidity of our room (use case). The sensor basically has 3 pins. VCC pin is for the power supply which ranges from 3.5V to 5.5V, The Data pin outputs both temperature and humidity through serial data, and the last one is connected to the ground of the circuit.

Operating Voltage: 3.5V to 5.5V
Temperature: 0 to 50 Celsius
Humidity: 20 to 80%
Output: Digital signal

In the code, we used the adafruit library and the time library. Installing the required libraries is the first step for data acquisition. Install adafruit module using the command sudo pip3 install Adafruit_DHT. 
 
We should connect the sensor's ground pin to the ground of the raspi, connect the positive terminal of the sensor to the 5v of the raspi  and connect the sensor's signal pin GPIO pin 4. After all this is done we'll see a red LED on the DHT11 sensor. Now we are ready to record the data.

We then establish the sensor and pins in the code. Then we capture the humidity and temperature into variables with the same name as temperature and humidity. And then we must print these recorded values onto our screen. We used an if-and-else loop for this. As the DHT11 can only be checked once in a time of one second, we used the sleep function to pause around 3 seconds between the checks.

Then we ran our code using the function python3 Rapi.py in the terminal.
Our code successfully ran and we captured the humidity and temperature of the room in the span of every 3 seconds in the terminal window. The following are the results obtained:
 
The results have been verified with the online temperature and humidity calculator. The results are the same as the online ones.
In our assignment, we used Raspberry Pi to measure the temperature and humidity of the place, but there are many more uses of it. Some of them include agriculture usage, data logging, and home automation (monitoring the environmental conditions in our home) and we can use it as our personal weather station for our daily uses.



