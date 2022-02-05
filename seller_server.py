#!/usr/bin/python3
from Connection import socket_connection
from product import inventory
import socket 
import json
import pickle

class seller_server:
    
    def put_item(self,seller_id,item):
        product_db = inventory.get_db_instance()
        return product_db.put_item(item,seller_id)
    
    def update_price(self,seller_id,item_id,price):
        product_db = inventory.get_db_instance()
        return product_db.update_item(item_id,key='sale_price',value=price)   
        
    def remove_item(self,seller_id,item_id,quantity):
        product_db = inventory.get_db_instance()
        return product_db.update_item(item_id,key='quantity',value=quantity)
        
    def display_item(self,seller_id):
        product_db = inventory.get_db_instance()
        item_list = product_db.get_item_by_seller_id(seller_id)
        return item_list
    
    def printDB(self):
        product_db = inventory.get_db_instance()
        redisDB = product_db.redisDB
        print("PRODUCT DB STATE NOW ",pickle.loads(product_db.redisDB.get("productDB")))

    def adapter(self,data):
        data = data.decode('utf-8')
        data = json.loads(data)
        try :
            if 'operation' in data:
                if data['operation'] == 'put_item':
                    seller_id = data['seller_id']
                    item = data['item']
                    return self.put_item(seller_id,item)
                elif data['operation'] == 'update_price':
                    print("Check the value "+str(data['item_id']))
                    seller_id = data['seller_id']
                    item_id = data['item_id']
                    price=data['price']
                    return self.update_price(seller_id,item_id,price)
                elif data['operation'] == 'remove_item':
                    seller_id = data['seller_id']
                    item_id = data['item_id']
                    quantity = data['quantity']
                    if quantity < 0:
                        return (-1,"Quantity cannot be less than 0")
                    return self.remove_item(seller_id,item_id,quantity)
                elif data['operation'] == 'display_item':
                    seller_id = data['seller_id']
                    return self.display_item(seller_id)
                elif data['operation'] == 'printDB':
                    self.printDB()
                    return True
                else: 
                    return "Not a valid operation"
            else:
                return "Invalid Input"
        except Exception as e:
            print("Error occured while parsing input data "+str(e))
            return str(e)    
    
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
                        conn.sendall(json.dumps(response).encode('utf-8'))
        except Exception as e:
            print("Closing the connection "+str(e))
            sock.close()               
                

def main():
    print("Starting Seller Server !!")
    s = seller_server()
    s.start_server()
    print("Seller Server is UP !!")
  
  
if __name__=="__main__":
    main()

                

