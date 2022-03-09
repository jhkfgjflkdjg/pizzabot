# pizza bot program
# 27/02/2022
#Bugs - phone number input allows letters
#     - name input allows numbers 

import random
from random import randint 

# List of random names 
names =["Mikara","Jodek","Tomas","Carlos","Karlo","Louis","Joaquin","Shawn","Marcus","Gabe"]
#List of pizza names 
Pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese ','Italian','Veggie','Vegan','Chicken Deluxe',
                'Mega Meat Lovers','Seafood Deluxe','Apricot chicken Deluxe','BBQ Chicken Deluxe']
#List of pizza prices 
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#List to store orderd pizzas 
order_list=[]
#List to store pizzas prices    
order_cost=[]

#customer detalis dictionary
customer_details = {}

#Validate inputs to check if they are blank
def not_blank(question):
    valid = False 
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank")


def welcome():
    ''' 
    Purpose: To generate a random name from the list and print out 
    a welcome message
    parameter: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dream Pizza***")
    print("*** My name is",name, "***")
    print("*** I will be here to help you order your delicious Dream Pizza***")

#menu for pickup and delivery 

def order_type(): 
 del_pick= ""
 print ("Is your order for pickup or delivery?")
 print ("For pickup please enter 1")
 print ("For delivery please enter 2")
 while True:
    try: 
     delivery = int(input("please enter a number"))
     if delivery >= 1 and delivery <= 2:  
        if delivery == 1:
            print ("pickup") 
            pickup_info()
            del_pick = "pickup"
            break
        
        elif delivery == 2:
            print ("delivery")
            delivery_info()
            del_pick = "delivery" 
            break 
     else:
         print ("Number must be 1 or 2")
    except ValueError:
      print("That is not a valid number")
      print("please enter 1 or 2")
 return del_pick 


#pick up information- name and phone number 
def pickup_info():
    question = ("please enter your name ")
    customer_details['name'] = not_blank(question )
    print (customer_details['name']) 
        
    question = ("please enter your phone number")
    customer_details ['phone'] = not_blank(question )
    print (customer_details ['phone'])
    print(customer_details)

# Delivery information - name address and phone
def delivery_info():
    question = ("please enter your name ")
    customer_details['name'] = not_blank(question )
    print (customer_details['name']) 
        
    question = ("please enter your phone number")
    customer_details ['phone'] = not_blank(question )
    print (customer_details ['phone'])

    question = ("please enter your house number ")
    customer_details ['house'] = not_blank(question )
    print (customer_details['house'])

    question = ("please enter your street name")
    customer_details ['street'] = not_blank(question )
    print (customer_details['street'])

    question = ("please enter your suburb")
    customer_details ['suburb'] = not_blank(question )
    print (customer_details['suburb'])
   

# pizza menu 
def menu():
    number_pizza = 12

    for count in range (number_pizza):
        print("{} {} ${:.2f}" .format(count+1,Pizza_names[count],pizza_prices[count]))


#choose total number of Pizzas - max 5
# Pizza order - from menu - print each pizza ordered with cast
def order_pizza():
    # ask for total number of pizza for order
    num_pizzas = 0

    while True:
        try:
            num_pizzas = int(input("How many pizza do you want to order? "))
            if num_pizzas >= 1 and num_pizzas <=5:
                break  
            else:
                print("Your order must be between 1 and 5") 
        except ValueError:
            print("That is not valid number")
            print("Please enter 1 or 5")
    #choose pizza from menu 
    for item in range(num_pizzas):
        while num_pizzas > 0:
            while True:
                try:
                    num_pizzas = int(input("please choose your pizzas by entering the number from the menu "))
                    if num_pizzas >= 1 and num_pizzas <=12:
                      break  
                    else:
                        print("Your pizza order must be between 1 and 12") 
                except ValueError:
                    print("That is not valid number")
                    print("Please enter a number between 1 and 12")
            pizza_ordered = int(input())
            pizza_ordered = pizza_ordered -1
            order_list.append(Pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            print("{} ${:.2f}" .format(Pizza_names[pizza_ordered],pizza_prices[pizza_ordered]))
            num_pizzas = num_pizzas -1 



#print order out - Including if order is delivery or pickup and names and prices of each pizza - total cost including any delivery charge 
def print_order(del_pick):
    total_cost = sum(order_cost)
    print("Customer_Details")
    if del_pick =="pickup":
         print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "delivery":
         print(f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Order Deatils")
    count= 0  
    for item in order_list:
        print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}") 


#Ability to cancel or proceed with order 





# main fuction 
def main():   
    ''' 
    Purpose: To run all fuctions 
    a welcome message 
    parameter: None
    Returns: None
    '''
    welcome()
    del_pick = order_type()
    print(del_pick)
    menu()
    order_pizza()
    print_order(del_pick)
    

main ()