# 1. Add new food items. Food Item will have the following details:
#         🔴 FoodID //It should be generated automatically by the application.
#         🔴 Name
#         🔴 Quantity. For eg, 100ml, 250gm, 4pieces etc
#         🔴 Price
#         🔴 Discount
#         🔴 Stock. Amount left in stock in the restaurant.
# 2. Edit food items using FoodID.
# 3. View the list of all food items.
# 4. Remove a food item from the menu using FoodID.
import json
import random
class Admin:
    def __init__(self):
        self.food = {}
    
    def Add_Food_Items(self):
        self.food_id = random.randint(1,10000)
        self.food_name = input("Enter Food Name : ")
        self.quantity = input("Enter food quantity: ")
        self.price = float(input("Enter Price of Food: "))
        self.discount = input("Enter discount on Food: ")
        self.stock = input("Enter the stock for this Food: ")
        self.item = {"Food_Id":self.food_id, "Food_Name":self.food_name, "Food_Quantity":self.quantity, "Food_Price":self.price, "Food_Discount":self.discount, "Food_Stock":self.stock}
        self.food[self.food_id] = self.item
        with open("food.json", "w") as f:
            json.dump(self.food,f,indent =4)
        print("Food Item added successfully...")
        return self.food
    
    def Edit_Food_Items(self):
        with open("food.json", "r") as f:
            data = json.load(f)
        for k,v in data.items():
            print("Food__Id: ",k,"Food_Item: ",v)
        id = str(input("Enter the Food_Id you want to edit: "))
        field = str(input("Enter the Field you want to edit: "))
        updated_value = str(input("Enter the updated value: "))
        data[id][field]=updated_value
        with open("food.json","w") as f:
            json.dump(data, f, indent=4)
        print("Food item edited successfully....")
        return self.food
    
    def View_Food_Items(self):
        with open("food.json","r") as f:
            ele = json.load(f)
        for k, v in ele.items():
            print("Food_Id: ", k,"Food_Item: ",v)
        
    def Remove_Food_Id(self):
        with open("food.json", "r") as f:
            data = json.load(f)
        for k, v in data.items():
            print("Food_Id: ",k,"Foof_Item: ",v)
        id = str(input("Enter the Food_Id you want to delete: "))
        del data[id]
        print("Selected food item has been deleted")
        with open("food.json","w") as f:
            json.dump(data,f,indent=4)
        return self.food
    
