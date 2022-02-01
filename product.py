#!/usr/bin/python3
from ast import Pass


class inventory():
    inv = None
    __instance = None
    lst = [0]*10
    
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
        self.inv = {'items':[]}
        print("Inventory called")
    
    def get_item_id(self,category_id):
        val = self.lst[category_id]
        self.lst[category_id] = val + 1
        return val
    
    def put_item(self, item):
        print("Put item function called")
        #generate ID
        #Keep number for each category 
        item_id = self.get_item_id(item['category_id'])
        item['item_id'] = item_id
        self.inv['items'].append(item)
        return item_id
    
    def search_item(self,category_id,keyword):
        item_lst = self.inv["items"]
        search_items = []
        for item in item_lst:
            if item["category_id"] == category_id:
                item_keywords = item["keyword"]
                for value in keyword:
                    if value in item_keywords:
                        search_items.append(item)
                        break
        return search_items
        
    # def delete_item(self, item):
    #     print("delete item function called")
    #     Pass
        
    # def get_item(self, item):
    #     print("get item function called")
    #     Pass
        
    def update_item(self,item_id,key,value):
        item_lst = self.inv["items"]
        for item in item_lst:
            if item["item_id"] == item_id:
                item[key] = value
                break
        self.inv["items"] = item_lst
        
    def get_item_by_seller_id(self,seller_id):
        item_by_seller = []
        item_lst = self.inv["items"]
        for item in item_lst:
            if item["seller_id"] == seller_id :
                item_by_seller.append(item)
        return item_by_seller
    

    