import serial

#cnx = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
cnx = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
cnx.flush()

def sendRequestVoltage():
    if cnx.in_waiting >0:
        line = cnx.readline().decode('utf-8').rstrip()
        #print(f"volt from arduino {line}")
        cnx.write(b"volt\n")
        return line
