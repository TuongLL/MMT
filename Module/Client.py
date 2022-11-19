import socket
import threading


class Listener:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip_and_port = ('127.0.0.1', 12345)
        self.node.bind(ip_and_port)
        self.node.listen(5)
        self.connection, addr = self.node.accept()

    def send_message(self, message):
        self.connection.send(message.encode())

    def receive_message(self):
        while True:
            data = self.connection.recv(1024).decode()
            print(data)


class Speaker:
    def __init__(self):
        self.node = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip_and_port = ('127.0.0.1', 12345)
        self.node.connect(ip_and_port)

    def send_message(self, message):
        self.node.send(message.encode())

    def receive_message(self):
        while True:
            data = self.node.recv(1024).decode()
            print(data)


def run():
    name = input("Type your name: ")
    start = input("Want to start a conversation? Y/N: ")
    if start == "Y":
        client = Speaker()
    else:
        client = Listener()
    always_receive = threading.Thread(target=client.receive_message)
    always_receive.daemon = True
    always_receive.start()
    while True:
        message = input()
        client.send_message(name + ': ' + message)


run()
