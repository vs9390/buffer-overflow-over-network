#!/usr/bin/env python2

import socket
import time

for i in range(50, 120, 10):
    HOST = '127.0.0.1'
    PORT = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    msg = ("A" * i)
    print "#" * 100
    print "Request Data"
    print msg + " - " + str(len(msg))

    try:
        s.connect((HOST, PORT))
    except:
        print "FAILED. Sleep briefly & try again"
        time.sleep(2)
        continue
    s.sendall(msg)

    received_data = s.recv(1024)
    print "Response Data"
    print received_data + " - " + str(len(received_data))
    s.close()