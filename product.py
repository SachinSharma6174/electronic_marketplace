#!/usr/bin/python3
from ast import Pass

class inventory():
    inv = None
    __instance = None
    item_id = 0
    
    @staticmethod
    def get_db_instance():
        if inventory.__instance == None:
            inventory()
            print("initializing the inventory")
            inventory.__instance.inv = {'items':[]}
        return inventory.__instance
    
    def __init__(self) -> None:
        if inventory.__instance != None:
            raise Exception("This is a singleton class")
        else:
            inventory.__instance = self
    
    def get_item_id(self):
        print("get item called")
        val = self.item_id
        self.item_id = val + 1
        return val
    
    def put_item(self, items,seller_id):
        print("Put item function called")
        #generate ID
        #Keep number for each category
        # check if item is already there. 
        item_ids = []
        for item in items:
            flag = 0
            item["seller_id"] = seller_id
            item_lst = self.inv["items"]
            #Check if the item already exists. If yes update the item. 
            for db_item in item_lst:
                if item["name"] == db_item["name"] and \
                    item["category_id"] ==  db_item["category_id"] and \
                    item["seller_id"] == db_item["seller_id"] : 
                        print("Item already exists")
                        item['item_id'] = db_item['item_id']
                        self.inv['items'].remove(db_item)
                        self.inv['items'].append(item)
                        
                        item_ids.append(db_item['item_id'])
                        flag = 1
                        break
            if flag == 0:
                item_id = self.get_item_id()
                item_ids.append(item_id)
                item['item_id'] = item_id
                print("Item Id recieved "+str(item_id))
                self.inv['items'].append(item)
        print(self.inv)
        return (item_ids)
    
    def search_item(self,category_id,keyword):
        item_lst = self.inv["items"]
        search_items = []
        for item in item_lst:
            print("Searching for item")
            if item["category_id"] == category_id:
                item_keywords = item["keyword"]
                for value in keyword:
                    if value in item_keywords:
                        search_items.append(item)
                        break
        print(self.inv)
        return search_items
        
    def update_item(self,item_id,key,value):
        item_lst = self.inv["items"]
        flag = 0
        for item in item_lst:
            if item["item_id"] == item_id:
                item[key] = value
                flag = 1
                break
        if flag == 1:
            self.inv["items"] = item_lst
            print(self.inv)
            return "Updated "+str(item_id)+" "+str(key)+" to "+str(value)
        else: 
            return "No such item item found."
        
    def get_item_by_seller_id(self,seller_id):
        item_by_seller = []
        item_lst = self.inv["items"]
        for item in item_lst:
            if item["seller_id"] == seller_id :
                item_by_seller.append(item)
        return item_by_seller

    