#!/usr/bin/python3
import socket 

class socket_connection():
        
    def make_connection(self,host,port):
        conn = socket.socket()
        conn.bind((host,port))
        conn.listen()
        return conn