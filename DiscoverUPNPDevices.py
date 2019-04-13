import socket

message = ("M-SEARCH * HTTP/1.1\r\n" \
    "HOST:239.255.255.250:1900\r\n" \
    "ST:upnp:rootdevice\r\n" \
    "MX:2\r\n" \
    'MAN:"ssdp:discover"\r\n' \
    "\r\n")

#UDP socket
#---------------------------------------------------------------------------------
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
udpSocket.settimeout(5)

#UPnP discovery (SSDP)
#---------------------------------------------------------------------------------
udpSocket.sendto(message.encode("utf-8"), ("239.255.255.250", 1900) )

try:
    while True:
        data, address = udpSocket.recvfrom(1024)
        print (address, data)
except socket.timeout:
    pass