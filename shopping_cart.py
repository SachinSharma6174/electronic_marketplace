#!/usr/bin/python3
from ast import Pass

class shopping_cart():
    cart = None
    __instance = None
    
    
    @staticmethod
    def get_db_instance():
        if shopping_cart.__instance == None:
            shopping_cart()
        return shopping_cart.__instance
    
    def __init__(self) -> None:
        if shopping_cart.__instance != None:
            raise Exception("This is a singleton class")
        else:
            shopping_cart.__instance = self
        self.cart = {'item':'nothing'}
        print("Shopping cart called")
    
    def add_item(self,buyer_id,item_id,quantity):
        if buyer_id in self.cart:
            item_dict = self.cart[buyer_id]
            item_dict[item_id] = quantity
        else:
            self.cart[buyer_id] = {item_id:quantity}
        print("Add item function called")
        Pass
        
    def remove_item(self,buyer_id,item_id,quantity):
        print("Remove item function called")
        if buyer_id in self.cart:
            item_dict = self.cart[buyer_id]
            item_dict[item_id] = quantity
        else:
            self.cart[buyer_id] = {item_id:quantity}
        return "Ok"
    
    def clear_cart(self,buyer_id):
        print("Clear cart function called")
        if buyer_id in self.cart:
            del self.cart[buyer_id]
            return "Ok"
        else:
            return "Cart is empty"
    
    def display_cart(self,buyer_id):
        print("Display cart function called")
        if buyer_id in self.cart:
            return self.cart[buyer_id]
        else:
            return "Empty cart"
    

    