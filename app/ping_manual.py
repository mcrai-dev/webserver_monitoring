import os
import subprocess
def popPing(host):
	response = subprocess.Popen(['ping', '-c 4',host], stdout=subprocess.PIPE)
	out = response.communicate()[0]
	return out


res = popPing("127.0.0.1")
print(res)
