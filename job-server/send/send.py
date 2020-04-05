import zmq
from time import sleep

def send():
    context = zmq.Context()
    send_socket = context.socket(zmq.PUSH)
    send_socket.bind("tcp://0.0.0.0:5557")

    sleep(5) #Allow sockets to connect
    for i in range(60):
        send_socket.send_string(str(i))
        print("sending: {}".format(i))
        sleep(1)

send()
