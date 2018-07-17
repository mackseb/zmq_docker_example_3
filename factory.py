import zmq
import threading

class Subscriber(object):

    def __init__(self):
      self.socket_sub = zmq.Context().socket(zmq.SUB)
      self.connect()

    def connect(self):
        self.socket_sub.connect("ipc://soc.ipc")
        self.socket_sub.setsockopt_string(zmq.SUBSCRIBE, '')
    
    def run(self):
        for _ in range(1000):
            print("sub received: " + self.socket_sub.recv_string())

    def start(self):
        threading.Thread(target=self.run).start()


class Publisher(object):

    def __init__(self):
      self.socket_pub = zmq.Context().socket(zmq.PUB)
      self.connect()

    def connect(self):
        self.socket_pub.bind("ipc://soc.ipc")
    
    def run(self):
        for i in range(2000):
            self.socket_pub.send_string("Hello")

    def start(self):
        threading.Thread(target=self.run).start()
            


if __name__ == "__main__":
    print("test")
    s1 = Subscriber()
    s2 = Publisher()

    s1.start()
    s2.start()