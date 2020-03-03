import socket
import sys
import time 

def get_client_id():
    id = sys.argv[1]
    return id

def client(id = 0):
    TCP_IP = "127.0.0.1"
    TCP_PORT = 5000
    BUFFER_SIZE = 1024
    delay = int(sys.argv[2])
    repeat = int(sys.argv[3])
    count = 0
    message = "ping"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((TCP_IP, TCP_PORT))
    except:
        print("Connection Error")
        sys.exit()

    while count != repeat:
        s.send(f"Client {id}: {message}".encode())
        print(f"Sending data: {message}")
        data = s.recv(BUFFER_SIZE)
        data = data.decode()
        print(f"Received from Server: {data}")
        count += 1
        time.sleep(delay)
    s.send("QUIT".encode())

if __name__ == "__main__":
    client(get_client_id())

'''
def client(id = 0):
    TCP_IP = "127.0.0.1"
    TCP_PORT = 5000
    BUFFER_SIZE = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((TCP_IP, TCP_PORT))
    except:
        print("Connection Error")
        sys.exit()
        
    print("Enter 'QUIT' to exit")
    message = input()

    while message != 'QUIT':
        s.send(f"Client {id}: {message}".encode())
        data = s.recv(BUFFER_SIZE)
        data = data.decode()
        print(f"Received from Server: {data}")
        message = input()
    s.send("QUIT".encode())

if __name__ == "__main__":
    client(get_client_id())
'''
