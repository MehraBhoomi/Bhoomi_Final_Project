import sys
from Admin import*
from User import*
admin = Admin()
user = User()

while True:
    print("Press 1 if Admin...")
    print("Press 2 if User...")
    print("Press 3 for Exit()...")
    choice = int(input("Enter your choice:  "))
    if choice==1:
        print("***************************Welcome To Admin Page****************************")
        print("Press 1 to add a food item...")
        print("Press 2 to edit a existing food item...")
        print("Press 3 to view all the  food item...")
        print("Press 4 to remove a food item...")
        number = int(input("Enter your choice:  "))
        if number==1:
            num = int(input("Enter the number of food items you want to add: "))
            for i in range(1,num+1):
                admin.Add_Food_Items()
        elif number==2:
            num = int(input("Enter the number of food items you want to edit: "))
            for i in range(1,num+1):
                admin.Edit_Food_Items()
        elif number==3:
            admin.View_Food_Items()
        elif number==4:
            num = int(input("Enter the number of food items you want to remove: "))
            for i in range(1,num+1):
                admin.Remove_Food_Id()
        else:
            print("Invalid number choice entered:   ")
    elif choice==2:
        print("********************************Welcome to user page***********************************")
        print("Press 1 for registration...")
        print("Press 2 to log in ...")
        print("Press 3 to place a new order...")
        print("Press 4 to view your order history...")
        print("Press 5 to edit profile...")
        number = int(input("Enter your choice:  "))
        if number==1:
            num = int(input("Enter the number of people you want to register: "))
            for i in range(1,num+1):
                user.Registration()
        elif number==2:
            user.Login()
        elif number==3:
            num = int(input("Enter the number of food items you want to order: "))
            for i in range(1,num+1):
                user.Place_new_order()
        elif number==4:
            user.Order_history()
        elif number==5:
            user.Edit_Profile()
        else:
            print("Please enter valid details....")
    elif choice ==3:
        print("************************Thank you using our application********************************")
        sys.exit()