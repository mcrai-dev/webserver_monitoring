import time
import Adafruit_ADS1x15


adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

while True:

	value = adc.read_adc(0, gain=GAIN)
	print("voltage: {:.2f} V".format(value *0.000125))
	time.sleep(1)
#	value = adc.read_adc(0, gain=GAIN)
#	VAC = (value * 2.048)/(GAIN*32767)
#	print("voltage: {:.2f} V".format(VAC ))
	time.sleep(1)
