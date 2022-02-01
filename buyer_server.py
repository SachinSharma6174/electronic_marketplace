#!/usr/bin/python3
from ast import keyword, operator
import imp
from unicodedata import category
from Connection import socket_connection
from product import inventory
from shopping_cart import shopping_cart
import socket 
import json


class client_server():
    
    def search_item(self,category_id,keywords):
        product_db = inventory.get_db_instance()
        return "Ok"
    
    def add_item(self,buyer_id,item_id,quantity):
        cart = shopping_cart.get_db_instance()
        return "Ok"
    
    def remove_item(self,buyer_id,item_id,quantity):
        cart = shopping_cart.get_db_instance()
        return "Ok"
    
    def clear_cart(self,buyer_id):
        cart = shopping_cart.get_db_instance()
        return "Ok"
    
    def display_cart(self,buyer_id):
        cart = shopping_cart.get_db_instance()
        return "Ok"

    def adapter(self, data):
        try:
            data = data.decode('utf-8')
            data = json.loads(data)
            if 'operation' in data:
                if data['operation'] == 'search_item':
                    category_id = data['category_id']
                    keywords = data['keywords']
                    self.search_item(category_id,keywords)
                elif data['operation'] == 'add_item':
                    buyer_id = data['buyer_id']
                    item_id = data['item_id']
                    quantity = data['quantity']
                    self.add_item(buyer_id,item_id,quantity)
                elif data['operation']  == 'remove_item':
                    buyer_id = data['buyer_id']
                    item_id = data['item_id']
                    quantity = data['quantity']
                    self.remove_item(buyer_id,item_id,quantity)
                elif data['operation'] == 'clear_cart':
                    buyer_id = data['buyer_id']
                    self.clear_cart(buyer_id)
                elif data['operation'] == 'display_cart':
                    buyer_id = data['buyer_id']
                    self.display_cart(buyer_id)
            else:
                return "Invalid Input"     
        except Exception as e:
            print("Error occured while parsing input data")
            return str(e)  

    def start_server(self):
        host='127.0.0.1'
        port=1500
        connection = socket_connection()
        try:
            sock = connection.make_connection(host,port)
            while True:
                conn, addr = sock.accept()
                with conn:
                    print("Connected by "+str(addr))
                    while True:
                        data = conn.recv(4096)
                        if not data:
                            break
                        response = self.adapter(data)
                        conn.sendall(json.dumps(response).encode('utf-8'))
        except Exception as e:
            print("Closing the connection "+str(e))
            sock.close()    
        

def main():
    print("Starting Buyer Server !!")
    c = client_server()
    c.start_server()
    print("Buyer Server is UP !!")
  
  
if __name__=="__main__":
    main()


                