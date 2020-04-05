import zmq
from time import sleep

def printRecv():
    context = zmq.Context()
    recv_socket = context.socket(zmq.PULL)
    recv_socket.bind("tcp://0.0.0.0:5555")

    while True:
        resp = recv_socket.recv_string()
        print("{}".format(resp))

printRecv()
