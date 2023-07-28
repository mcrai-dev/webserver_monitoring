import psutil
import time

def get_cpu_percent():
	return psutil.cpu_percent(1)
