import socket
import sys

#create a socket
def create_socket():
    try:
        global host 
        global port 
        global s
        host = "127.0.0.1"
        port = 22
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error : " + str(msg))

# Binding the socket and listening for connections 
def bind_socket():
    try:
        global host 
        global port 
        global s
        print ("Binding the port : " + str(port))
        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("socket binding error : " + str(msg) + "\n" + "Retrying....")
        bind_socket

# Accept a connection, establish connection 
def accept_socket():
    conn, address = s.accept()
    print("Connection has been established |" + "IP" + address[0] + "| Port" + str(address[1]))
    send_commands(conn)
    conn.close()

#send commands to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    accept_socket()


main()
