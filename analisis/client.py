import zmq

import csv
import datetime

inicio = datetime.datetime(2013, 10, 23, 14, 37, 50, 0)

 
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5000")
socket.setsockopt(zmq.SUBSCRIBE, "ecobici1 bici")
 
while True:
    d = socket.recv().split()
    print  inicio+datetime.timedelta(milliseconds=int(d[2]))

