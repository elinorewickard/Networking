"""
Elinore Wright
Networking software
"""

import threading
import socket

#localhost server ip
host = '127.0.0.1' 
port = 50000

#creating server and putting into listen - its listening for a connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    """passes a message to all the clients"""
    for client in clients:
        client.send(message)

def handle(client):
    """Makes sure that each client is recieving the message
    if not, the client is removed and a message sharing that is
    printed to all the clients"""
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()

            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break

#main function basically
def receive():
    """handles all the client connections"""
    while True:
        client, address = server.accept()
        #prints on server
        print(f"Connected with {str(address)}")

        #code word, supposed to be the nickname from client
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        #keep clients & nicknames paired at same index in both lists
        nicknames.append(nickname)
        clients.append(client)
        
        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat'.encode("ascii"))
        client.send("Connected to the server".encode("ascii"))

        #allows server to handle multipule clients easier, stops program from hanging
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening...")
receive()