import socket
import threading

PORT = 7447
MESSAGE_SIZE = 64
ENCODING = 'utf-8'

def main():
    address = socket.gethostbyname(socket.gethostname())
    host_information = (address, PORT)
    # print(address)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(host_information)

    print("server is waiting ...")
    waiting(s)

def waiting(server):
    server.listen()
    while True:
        conn, address = server.accept()

        t = threading.Thread(target=handle_client, args=(conn, address))
        t.start()

def handle_client(conn, address):
    print(" connection is started from {}".format(address))

    connected = True
    while connected:
        message_length = int(conn.recv(MESSAGE_SIZE).decode(ENCODING))
        msg = conn.recv(message_length).decode(ENCODING)

        print("message : {}".format(msg))

        if msg == "DISCONNECTED":
            connected = False
    conn.close()




if __name__ == '__main__':
    main()