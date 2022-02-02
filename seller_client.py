#!/usr/bin/python3
import socket
import json
from subprocess import call
from unicodedata import category 


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1200      # The port used by the server

def put_item(seller_id,item):
    data = {'operation':'put_item','item':item,'seller_id':seller_id}
    response = call_seller_sever(data)
    return response

def update_price(seller_id,item_id,price):
    data = {'operation':'update_price','seller_id':seller_id,'item_id':item_id,'price':price}
    call_seller_sever(data)

def remove_item(seller_id,item_id,quantity):
    data = {'operation':'remove_item','seller_id':seller_id,'item_id':item_id,'quantity':quantity}
    call_seller_sever(data)
    
def display_item(seller_id):
    data = {'operation':'display_item','seller_id':seller_id}
    response = call_seller_sever(data)

def call_seller_sever(data):
    data = json.dumps(data).encode('utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("initiating connection")
        s.connect((HOST, PORT))
        s.sendall(data)
        data = s.recv(1024)

    print('Received', repr(data))
    data = data.decode('utf-8')
    return json.loads(data)
    
def main():
    item = [{"name":"Pen","category_id":0,"keywords":["pen","stationary","ink","pencil","school supplies"],"condition":"new","sale_price":2.5,'quantity':5},\
        {"name":"Pencil","category_id":0,"keywords":["pencil","stationary","ink","pencil","school supplies"],"condition":"new","sale_price":1,'quantity':10}]
    # During login api caller seller client will recieve seller_id
    seller_id = '123'
    item_ids = put_item(seller_id,item)
    if (item_ids[0] == -1):
        print("Error recived")
        return
    update_price(seller_id,item_ids[0],2)
    remove_item(seller_id,item_ids[1],3)
    display_item(seller_id)
  
if __name__=="__main__":
    main()

   



