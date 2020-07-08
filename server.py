import socket

ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ms.bind(("0.0.0.0", 1111))
ms.listen()

while True:
    conn, addr = ms.accept()
    data = conn.recv(1000)
    if (data):
        print("Got a request!")

