# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
n = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

numMessages = int(n)
receivingPort = port + 1


for i in range(numMessages):
    data = "Message" + str(i)
    print(data)
    s.sendto(data.encode('utf-8'), server_address)

    print ("Waiting to receive ack on port %d : press Ctrl-C or Ctrl-Break to stop " % receivingPort)
    buf = s.recvfrom(port)
    if not len(buf):
        break
    print ("acknowledgment received: " + str(buf))

"""
while n>0:
    print ("Enter data to transmit: ENTER to quit")
    data = sys.stdin.readline().strip()
    if not len(data):
        break
#    s.sendall(data.encode('utf-8'))
    s.sendto(data.encode('utf-8'), server_address)
"""

#s.shutdown(1)
