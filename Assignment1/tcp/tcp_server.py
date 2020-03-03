import socket
import sys
from threading import Thread

def tcp_server():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5000
    BUFFER_SZIE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((TCP_IP, TCP_PORT))
    s.listen(5)
    print("Server started at port " + str(TCP_PORT))

    while True:
        conn, addr = s.accept()
        ip, port = str(addr[0]), str(addr[1])
        print(f"Connected with Client: {ip} {port}")
        try:
            Thread(target = client_thread, args = (conn, ip, port)).start()
        except:
            print(" failed tThreado start.")
    s.close()

def client_thread(conn, ip, port, BUFFER_SIZE = 1024):
    active = True
    while active:
        data = conn.recv(BUFFER_SIZE)
        data = data.decode()
        if data == "QUIT":
            print(f"Connection with Client: {ip} {port} closed")
            conn.close()
            active = False            
        else:
            print("Received data: " + data)
            conn.send("pong".encode())

if __name__ == "__main__":
    tcp_server()
