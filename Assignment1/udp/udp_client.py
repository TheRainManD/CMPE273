import socket
from socket import timeout


UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "ping"

'''
def send(id=0):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(f"{id}:{MESSAGE}".encode(), (UDP_IP, UDP_PORT))
        data, ip = s.recvfrom(BUFFER_SIZE)
        print("received data: {}: {}".format(ip, data.decode()))
    except socket.error:
        print("Error! {}".format(socket.error))
        exit()
'''

def get_client_id():
    id = input("Enter client id:")
    return id

def client(id = 0):
    sequence_num = 1
    delimiter = "|:|"
    final_message = "Upload successfully completed"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(1)
        print("Connected to the server.")
        file_1 = open("upload.txt","r")
        #for data in file_1:
        while True:
            data = file_1.readline()
            if not data:
                break
            ack_received = False
            while not ack_received:
                s.sendto((str(sequence_num) + delimiter + str(id) + ": " + data).encode(), (UDP_IP, UDP_PORT))
                try:
                    data_received, ip = s.recvfrom(BUFFER_SIZE)
                except timeout:
                    continue
                data_received = data_received.decode()
                ack = data_received.split(delimiter)[0]
                if int(ack) == sequence_num:
                    #message = data_received.split(delimiter)[1]
                    print(f"Received ACK({ack}) from the server {ip}.")
                    #print(f"Received from server: {ip}: {message}")
                    ack_received = True
                    sequence_num += 1
        s.sendto((final_message + delimiter + final_message).encode(), (UDP_IP, UDP_PORT))
        print("File upload successfully completed")
        file_1.close()
        s.close()
    except socket.error:
        print("Error! {}".format(socket.error))
        exit()
    #print(sequence_num)

if __name__ == "__main__":
    client(get_client_id())
