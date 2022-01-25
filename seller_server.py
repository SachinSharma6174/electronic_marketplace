#!/usr/bin/python3
from Connection import socket_connection
from product import inventory
import socket 

class seller:
    
    def put_item(self,seller_id,item,quantity):
        product_db = inventory.get_db_instance()
        item["seller_id"] = seller_id
        item["item_id"] = "123"
        item["quantity"] = quantity
        product_db.put_item(item)
        print("Add item called "+str(product_db.inv))
        return "Ok"
    
    def update_price(self,seller_id,item_id,price):
        product_db = inventory.get_db_instance()
        product_db.update_item(item_id,key='sale_price',value=price)
        return "Ok"
        
    def remove_item(self,seller_id,item_id,quantity):
        product_db = inventory.get_db_instance()
        product_db.update_item(item_id,key='quantity',value=quantity)
        return "Ok"
        
    def display_item(self,seller_id):
        product_db = inventory.get_db_instance()
        item_list = product_db.get_itemby_seller_id(seller_id)
        return item_list
    
    
    def start_server(self):
        host='127.0.0.1'
        port=1200
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
                        conn.sendall(response)
        except Exception as e:
            print("Closing the connection "+str(e))
            sock.close()
        
                
                
s = seller()
s.start_server()
                

