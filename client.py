import socket

PORT = 7447
MESSAGE_SIZE = 64
ENCODING = 'utf-8'

def main():
    address = socket.gethostbyname(socket.gethostname())
    server_information = (address, PORT)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(server_information)

    send_message(s, "HELLO WORLD")
    send_message(s, "DISCONNECTED")

def send_message(client, msg):
    message = msg.encode(ENCODING)

    msg_length = len(message)
    msg_length = str(msg_length).encode(ENCODING)
    msg_length += b' ' * (MESSAGE_SIZE - len(msg_length))

    client.send(msg_length)
    client.send(message)

if __name__ == '__main__':
    main()