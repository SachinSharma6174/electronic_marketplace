#!/usr/bin/python3
import socket
import json
from subprocess import call
from unicodedata import category 


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1500     # The port used by the server

def search_item(category_id,keywords):
    data = {'category_id':category_id,'keywords':keywords}
    response = call_buyer_sever(data)
    return response
    
def add_item(buyer_id,item_id,quantity):
    data = {'buyer_id':buyer_id,'item_id':item_id,'quantity':quantity}
    call_buyer_sever(data)
    return "Ok"
    
def remove_item(self,buyer_id,item_id,quantity): 
    data = {'buyer_id':buyer_id,'item_id':item_id,'quantity':quantity} 
    call_buyer_sever(data)
    return "Ok"
    
def clear_cart(self,buyer_id):
    data = {'buyer_id':buyer_id}
    call_buyer_sever(data)
    return "Ok"
    
def display_cart(self,buyer_id):
    data = {'buyer_id':buyer_id}
    call_buyer_sever(data)
    return "Ok"


def call_buyer_sever(data):
    data = json.dumps(data).encode('utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("initiating connection")
        s.connect((HOST, PORT))
        s.sendall(data)
        data = s.recv(1024)

    print('Received', repr(data))
    return data


def main():
    buyer_id = "123"
    items = search_item("1",["stationary","Pen"])
    add_item(buyer_id,items[0]["item_id"],"3")
    remove_item(buyer_id,items[0]["item_id"],"2")
    display_cart(buyer_id)
    clear_cart(buyer_id)
