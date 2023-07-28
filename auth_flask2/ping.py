import subprocess

def ping(host):
	response = subprocess.Popen(['ping', '-c 4',host], stdout=subprocess.PIPE)
	out = response.communicate()[0]
	return out
