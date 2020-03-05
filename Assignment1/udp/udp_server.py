import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = "pong"

'''
def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((UDP_IP, UDP_PORT))

    while True:
        # get the data sent to us
        data, ip = s.recvfrom(BUFFER_SIZE)
        print("{}: {}".format(ip, data.decode(encoding="utf-8").strip()))
        # reply back to the client
        s.sendto(MESSAGE.encode(), ip)

listen_forever()
'''

def udp_seq_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((UDP_IP, UDP_PORT))
    delimiter = "|:|"
    print("Server started at port " + str(UDP_PORT))
    print("Accepting a file upload: ")
    file1 = open("result.txt","w")
    final_message = "Upload successfully completed"

    while True:
        received_data, ip = s.recvfrom(BUFFER_SIZE)
        received_data = received_data.decode()
        ack = received_data.split(delimiter)[0]
        message = received_data.split(delimiter)[1]
        if message == final_message:
            print(final_message)
            break
        file1.write(message)
        print(f"Received from client: {ip}: {message}")
        s.sendto((ack + delimiter + MESSAGE).encode(), ip)

if __name__ == "__main__":
    udp_seq_server()
