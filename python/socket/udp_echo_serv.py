'''
udp_echo_serv.py
UDP Echo Server example
'''

import socket
import sys

BUFLEN = 8192

def udp_serve(sockfd):
    print "serving..."
    while True:
        msg, addr = sockfd.recvfrom(BUFLEN)
        print "received:" + msg
        sockfd.sendto(msg, addr)
        
        
if __name__ == '__main__' :
    arg_len = len(sys.argv)
    if arg_len != 3:
        print "usage :python udp_echo_serv.py serv_ip serv_port"
        print "example : python udp_echo_serv.py 127.0.0.1 6001"
        sys.exit(0)
        
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    s.bind((host, port))
    
    udp_serve(s)