import socket

def create_wol_packet(mac_address):
    #convert the mac address to a bytes object
    mac_bytes = bytes.fromhex(mac_address.replace(':', ''))
    #create the magic packet data
    data  = b'\xff' * 6 + mac_bytes * 16
    #create the socket and send the packet 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(data, ('255.255.255.255', 9))
