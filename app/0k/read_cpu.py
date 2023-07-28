import psutil
import time

def get_cpu():
	return psutil.cpu_percent(1)
	
if __name__=="__main__":
	while True:
		print(f"CPU = {get_cpu()} %")
		time.sleep(1)
		
