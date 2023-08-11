#  1. Register on the application. Following to be entered for registration:
#         🔴 Full Name             
#         🔴 Phone Number
#         🔴 Email                
#         🔴 Address
#         🔴 Password             
# 2. Log in to the application
# 3. The user will see 3 options:
#         🔴 Place New Orde   🔴 Order History    🔴 Update Profile
# 4. Place New Order: The user can place a new order at the restaurant.
#         🔵 Show list of food. The list item should as follows:
#             🔴 Tandoori Chicken (4 pieces) [INR 240]
#             🔴 Vegan Burger (1 Piece) [INR 320]
#             🔴 Truffle Cake (500gm) [INR 900]
# 5. Users should be able to select food by entering an array of numbers. 
#        For example, if the user wants to order Vegan Burger and Truffle Cake they should enter [2, 3]
# 6. Once the items are selected user should see the list of all the items selected. 
#        The user will also get an option to place an order.
# 7. Order History should show a list of all the previous orders
# 8. Update Profile: the user should be able to update their profile.

import random
import json
class User:
    def __init__(self):
        self.personal_details = {}
    def Registration(self):
        self.id_no = random.randint(1,10000)
        Full_Name = input("Enter your full name: ")
        Phone_no = input("Enter your contact number: ") 
        self.email = input("Enter your email_id: ")
        self.Password = input("Enter your Password: ") 
        Address = input("Enter your Address: ")    
        user_details = {"Full_Name":Full_Name,"Phone_no":Phone_no,"Email.id":self.email,"Address":Address,"Password":self.Password}
        self.personal_details[self.id_no] = user_details
        with open("user_details.json","w") as f:
            json.dump(self.personal_details,f,indent=4)
        print("You have successfully registered on our website.....")
        return self.personal_details
    
    def Login(self):
        print("Welcome to the login page")
        with open("user_details.json","r") as f:
            data = json.load(f)
        email = str(input("Enter ur email address: "))
        password = str(input("Enter your password: "))
        while True:
            if email in data:
                if password == data[self.id_no]["Password"]:
                    print("You have successfully log in.....")
                    break
                else:
                    print("Enter correct password")
            else:
                print("Enter registered email id ...")
                print("Visit Registration page if not registered yet...")

    def Place_new_order(self):
        self.Food_order_list =[]
        menu = [{"Food_item":"Tandoori Chicken","Quantity":"4 pieces","Price":680},
                {"Food_item":"Vegan Burger","Quantity":"1","Price":300},
                {"Food_item":"Truffle Cake","Quantity":"1","Price":900}]
        print("Here is your menu card....")
        for i in menu:
            print(f"Enter {menu.index(i)} for {i}")
            
        user_input = int(input("Enter the number for the food item you want to order: "))

        if user_input==0:
            self.Food_order_list.append(menu[0])
        elif user_input==1:
            self.Food_order_list.append(menu[1])
        elif user_input==2:
            self.Food_order_list.append(menu[2])
        else:
            print("Please choose from the menu....")
        
        print("Press 1 for order confirmation ")
        print("Press 2 for cancelling the order ")
        order = int(input("Enter your order choice: "))
        if order==1:
            print("order placed sucesfully")
        elif order==2:
            print("Your order has been canceled")
        return self.Food_order_list
        
    def Order_history(self):
        for i in self.Food_order_list:
            print("Here is the list of your ordered Food Items: ..")
            print("Your Order history is: ", i)
            return ""

    def Edit_Profile(self):
        with open("user_details.json", "r") as f:
            data = json.load(f)
        for k, v in data.items():
            print("Email:",k,"User details: ",v)

        mail_id = str(input("Enter the eamil id which you want to update: "))
        field = str(input("Enter the field which you want to update: "))
        updated_value = (input("Enter the updated value:"))
        data[mail_id][field]=updated_value
        with open("user_details.json","w") as f:
            json.dump(data,f, indent=4)
        return data

