import socket
import threading
import time

shutdown = False
client_join = False


def receiving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))
                time.sleep(0.2)
        except:
            pass


host = '127.0.0.1'
port = 0
server = ('127.0.0.1', 9090)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((host, port))
s.setblocking(0)

alias = input("Name: ")

thread = threading.Thread(target=receiving, args=("RecvThread", s))
thread.start()

while not shutdown:
    if not client_join:
        s.sendto(("[" + alias + "] => join chat ").encode("utf-8"), server)
        client_join = True
    else:
        try:
            message = input()
            if message != "":
                s.sendto(("[" + alias + "] :: " + message).encode("utf-8"), server)
            time.sleep(0.2)
        except:
            s.sendto(("[" + alias + "] <= left chat ").encode("utf-8"), server)
            shutdown = True

thread.join()
s.close()
