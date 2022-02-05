#!/usr/bin/python3
from Connection import socket_connection
from product import inventory
from shopping_cart import shopping_cart
import socket 
import json
import pickle

class client_server():
    
    def search_item(self,category_id,keywords):
        print("\nSearch Items Called")
        product_db = inventory.get_db_instance()
        response = product_db.search_item(category_id,keywords)
        print("\nRESPONSE ON BUYER SERVER",response)
        return response
    
    def add_item(self,buyer_id,item_id,quantity):
        cart = shopping_cart.get_db_instance()
        return cart.add_item(buyer_id,item_id,quantity)
    
    def remove_item(self,buyer_id,item_id,quantity):
        cart = shopping_cart.get_db_instance()
        return cart.remove_item(buyer_id,item_id,quantity)
    
    def clear_cart(self,buyer_id):
        cart = shopping_cart.get_db_instance()
        return cart.clear_cart(buyer_id)
    
    def display_cart(self,buyer_id):
        cart = shopping_cart.get_db_instance()
        return cart.display_cart(buyer_id)

    def printDB(self):
        product_db = inventory.get_db_instance()
        redisDB = product_db.redisDB
        print("BUYER PRODUCT DB STATE NOW ",pickle.loads(product_db.redisDB.get("productDB")))


    def adapter(self, data):
        try:
            data = data.decode('utf-8')
            data = json.loads(data)
            if 'operation' in data:
                if data['operation'] == 'search_item':
                    category_id = data['category_id']
                    keywords = data['keywords']
                    return self.search_item(category_id,keywords)
                elif data['operation'] == 'add_item':
                    buyer_id = data['buyer_id']
                    item_id = data['item_id']
                    quantity = data['quantity']
                    return self.add_item(buyer_id,item_id,quantity)
                elif data['operation']  == 'remove_item':
                    buyer_id = data['buyer_id']
                    item_id = data['item_id']
                    quantity = data['quantity']
                    return self.remove_item(buyer_id,item_id,quantity)
                elif data['operation'] == 'clear_cart':
                    buyer_id = data['buyer_id']
                    return self.clear_cart(buyer_id)
                elif data['operation'] == 'display_cart':
                    buyer_id = data['buyer_id']
                    return self.display_cart(buyer_id)
                elif data['operation'] == 'display_all_items':
                    self.printDB()
                    return True

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


                