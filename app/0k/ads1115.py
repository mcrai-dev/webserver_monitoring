import time
import board
import Adafruit_ADS1x15 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = board.I2C()
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.PO)


while True:

	value = chan.value
	VAC = (value*0.125)/1000
	print("voltage: {:.2f} V".format(VAC ))
	time.sleep(1)
