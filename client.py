#!/usr/bin/python3
import socket
import json
from unicodedata import category 


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1200      # The port used by the server

item = {'operation':'add','data':["category"]}
user_encode_data = json.dumps(item).encode('utf-8')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("initiating connection")
    s.connect((HOST, PORT))
    s.sendall(user_encode_data)
    data = s.recv(1024)

print('Received', repr(data))