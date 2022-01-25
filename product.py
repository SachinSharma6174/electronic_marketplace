#!/usr/bin/python3
    

from ast import Pass


class inventory():
    inv = None
    __instance = None
    
    
    @staticmethod
    def get_db_instance():
        if inventory.__instance == None:
            inventory()
        return inventory.__instance
    
    def __init__(self) -> None:
        if inventory.__instance != None:
            raise Exception("This is a singleton class")
        else:
            inventory.__instance = self
        self.inv = {'item':'nothing'}
        print("Inventory called")
        pass
    
    def put_item(self, item):
        print("Put item function called")
        Pass
        
    def delete_item(self, item):
        print("delete item function called")
        Pass
        
    def get_item(self, item):
        print("get item function called")
        Pass
        
    def update_item(self,item_id,key,value):
        Pass
        
    def get_itemby_seller_id(self,seller_id):
        Pass
    

    