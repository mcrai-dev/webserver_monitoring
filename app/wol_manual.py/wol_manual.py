import socket

acer_wfi = "08:6A:C5:AA:E2:F9"
acer_eth = "C0:18:50:4B:89:4D"

def create_wol_packet(mac_address):
    #convert the mac address to a bytes object
    mac_bytes = bytes.fromhex(mac_address.replace(':', ''))
    #create the magic packet data
    data  = b'\xff' * 6 + mac_bytes * 16
    #create the socket and send the packet 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    #pretend to wake on with broadcast
    sock.sendto(data, ("255.255.255.0", 9))


if __name__ == '__main__':
        create_wol_packet(acer_eth)