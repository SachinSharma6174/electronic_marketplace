#!/usr/bin/python3
from re import S
import socket
import json
from subprocess import call
from unicodedata import category 
import pickle
import time



HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1500     # The port used by the server

def search_item(category_id,keywords):
    print("\nBuyer Client :: /Search Items")
    data = {'operation':'search_item','category_id':category_id,'keywords':keywords}
    response = call_buyer_sever(data)
    print("\nSearch Item RESPONSE",response)
    return response
    
def add_item(buyer_id,item_id,quantity):
    data = {'operation':'add_item','buyer_id':buyer_id,'item_id':item_id,'quantity':quantity}
    return call_buyer_sever(data)
    
    
def remove_item(buyer_id,item_id,quantity): 
    data = {'operation':'remove_item','buyer_id':buyer_id,'item_id':item_id,'quantity':quantity} 
    return call_buyer_sever(data)
    
def clear_cart(buyer_id):
    data = {'operation':'clear_cart','buyer_id':buyer_id}
    return call_buyer_sever(data)
    
    
def display_cart(buyer_id):
    print("\nDisplay Cart for Buyer Id {}".format(buyer_id))
    data = {'operation':'display_cart','buyer_id':buyer_id}
    return call_buyer_sever(data)

def display_all_items():
    data = {'operation':'display_all_items'}
    call_buyer_sever(data)
    return "Ok"

def call_buyer_sever(data):
    data = json.dumps(data).encode('utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("initiating connection")
        s.connect((HOST, PORT))
        s.sendall(data)
        data = s.recv(8192)
    data = data.decode('utf-8')
    print("Response",data)
    return json.loads(data)

def main():
    # display_all_items()
    buyer_id = "123"
    start = time.perf_counter()
    items = search_item(0,["stationary","Pen"])
    end = (time.perf_counter()- start)*1000
    print("\nSearch API TAT {} ms".format(end))
    
    
    start = time.perf_counter()
    print(add_item(buyer_id,0,"3"))
    end = (time.perf_counter()- start)*1000
    print("\Add Item API TAT {} ms".format(end))

    start = time.perf_counter()
    print(remove_item(buyer_id,0,"2"))
    end = (time.perf_counter()- start)*1000
    print("\nRemove Items API TAT {} ms".format(end))


    start = time.perf_counter()
    print(display_cart(buyer_id))
    end = (time.perf_counter()- start)*1000
    print("\nDisplay Cart API TAT {} ms".format(end))


    start = time.perf_counter()
    print(clear_cart(buyer_id))
    end = (time.perf_counter()- start)*1000
    print("\n  Clear Cart API TAT {} ms".format(end))


if __name__=="__main__":
    main()
