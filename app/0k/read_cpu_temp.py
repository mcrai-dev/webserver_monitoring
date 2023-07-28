#from pyspectator.processor import Cpu 
from gpiozero import CPUTemperature
import time

while True :
	#cpu = Cpu(monitoring_latency=1)
	cpu = CPUTemperature()
	print(cpu.temperature)
	time.sleep(1)
