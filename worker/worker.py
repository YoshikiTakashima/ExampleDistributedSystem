import zmq
from datetime import datetime
from time import sleep

def work_loop(name):
    context = zmq.Context()
    in_socket = context.socket(zmq.PULL)
    in_socket.connect("tcp://kuroneko.andrew.cmu.edu:5557")
    out_socket = context.socket(zmq.PUSH)
    out_socket.connect("tcp://kuroneko.andrew.cmu.edu:5555")

    while True:
        inbound = in_socket.recv_string()
        #print("inbound: {}".format(inbound))
        dateTimeObj = datetime.now()
        out_socket.send_string("NODE: {}, ID: {}, DATE: {}".format(name, \
                                                                   inbound, \
                                                                   str(dateTimeObj)))

from sys import argv
work_loop(argv[1])
