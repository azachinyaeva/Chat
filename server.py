import socket
import time

host = '127.0.0.1'
port = 9090
print("[ Server IP: "+host+" ]")
clients = []
shutdown = False

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
print("[ Server Started ]")

while not shutdown:
    try:
        data, addr = s.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)

        local_time = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
        print("[" + local_time + "]/", end="")
        print(data.decode("utf-8"))

        for client in clients:
            if addr != client:
                s.sendto(data, client)
    except:
        print("\n[ Server Stopped ]")
        shutdown = True

s.close()
