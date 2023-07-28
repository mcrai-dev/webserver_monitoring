from gpiozero import CPUTemperature

def getCPUTemperature():
	cpu = CPUTemperature()
	return cpu.temperature
