import os

def ping(host):
    ip_list = [host]
    print(f"THE IP_LIST from string function is {ip_list}")
    for ip in ip_list:
        response = os.popen(f"ping {ip}"). read()
        print(f"The response is {response}")
    
ping('127.0.0.1')
