'''
UDP Echo Client
www.codernotes.com
'''

import socket
import sys

BUF_LEN = 4096

if __name__ == '__main__' :
    
    arg_len = len(sys.argv)
    
    if arg_len != 4:
        print "usage   : python udp_echo_client.py serv_ip serv_port message"
        print "example : python udp_echo_client.py 127.0.0.1 6001 hai"
        sys.exit(0)
        
    host = sys.argv[1]
    port = int(sys.argv[2])
    msg = sys.argv[3]
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s.connect((host,port))
    
    s.send(msg)
    
    print "sending:" + msg
    
    reply = s.recv(BUF_LEN)
    
    print "reply:" + reply