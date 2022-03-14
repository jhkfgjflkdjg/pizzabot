#Pizza bot program
#Bugs - phone number input allows letters
#     - Name input allows numbers
#Known bugs
# Final printout is not printing customer details correctly
#

import sys
import random
from random import randint



#list of random names
names = ["Mikara", "Jodek", "Marcus", "Tomas", "Joaquin", 
        "Justin", "Gabe", "Shawn", "Karlo", "Mnawel"]
#Customer detail dictionary 
customer_details = {}


#lists of pizza names
pizza_names =  ['Margherita', 'Pepperoni', 'Hawaiian', 'Cheese', 
                'Italian', 'Veggie', 'Vegan', 'Chicken Deluxe', 'Mega Meat Lovers', 
                'Seafood Deluxe', 'Apricot Chicken Deluxe', 'BBQ Chicken Deluxe' ]
#lists of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#list to store ordered pizzas
order_list =[]
#list to store pizza's prices 
order_cost =[]

#Validtes inputs to check if they are blank
def not_blank(question):
    valid = False
    while not valid: 
        response = input (question)
        if response != "":
            return response.title() 
        else:
            print ("This cannot be blank")

#Validtes inputs to check if they are an integer.
def val_int(LOW, HIGH, question):
    while True:
        try:
            num = int(input(question))
            if num >= 1 and num <= 2:
                return num
            else: 
                print("Please enter a number between", LOW, "and" , HIGH)
        except ValueError:
            print ("That is not a valid number.")
            print ("Please enter a number between", LOW, "and" , HIGH)





# Welcome message with random name
def welcome():
    """
Purpose: To generate a random name from the list and print out a welcome message 
Parameters: None 
Returns: None

    """
    
    
    num = randint(0,9)
    name = (names[num])
    print("** Welcome to Dream Pizza **")
    print("** My name is", name ,"**")
    print("** I will be here to help you order your delicious Dream Pizza **")
# Menu for pickup or delivery 
def order_type():
    del_pick = ""
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between, {LOW} and {HIGH}")
    print ("Is your order for pickup or delivery?")
    print (" For pickup enter 1.")
    print (" For delivery enter 2.")
    delivery = val_int(LOW, HIGH, question)
    if delivery == 1:
        print ("Pickup")
        del_pick = "pickup"
        pickup_info()
        

    else:
        print ("Delivery")
        delivery_info()
        del_pick = "delivery"
    return del_pick



# Pick up information - name and phone number
def pickup_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    #print (customer_details ['name'])

    question = ("Please enter your phone number ")
    customer_details["phone"] = not_blank(question )
    #print (customer_details ['phone'])
    print(customer_details)


# Delivery information  - name, address and phone number

def delivery_info():
    question = ("Please enter your name ")
    customer_details['name'] = not_blank(question )
    print (customer_details ['name'])

    question = ("Please enter your phone number ")
    customer_details["phone"] = not_blank(question )
    print (customer_details ['phone'])

    question = ("Please enter your house number ")
    customer_details["house"] = not_blank(question )
    print (customer_details ['house'])

    question = ("Please enter your street name ")
    customer_details["street"] = not_blank(question )
    print (customer_details ['street'])

    question = ("Please enter your suburb ")
    customer_details["suburb"] = not_blank(question )
    print (customer_details ['suburb'])
 

# Pizza menu

def menu():
    number_pizzas = 12
    for count in range (number_pizzas):
        print("{} {} ${:.2f}"   .format(count+1,pizza_names[count],pizza_prices[count]  ))


# Choose total number of Pizzas - max 5 
# Pizza ordering - from menu - print each pizza ordered with cost 

def order_pizza():

    num_pizzas = 0
    LOW = 1
    HIGH = 5
    MENU_LOW = 1
    MENU_HIGH = 12
    question = (f"Enter a number between, {LOW} and {HIGH}") 
    print("How many pizzas do you want to order?")
    num_pizzas = val_int(LOW, HIGH, question)
    #choose pizza from menu
    for item in range(num_pizzas):
        while num_pizzas > 0 :
            print("Please choose your pizzas by entering" 
            "the number from the menu ")
            question = (f"Enter a number between, {MENU_LOW} and {MENU_HIGH} ")
            pizza_ordered = val_int(MENU_LOW, MENU_HIGH, question)
            pizza_ordered = pizza_ordered -1
            order_list.append(pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            print("{} ${:.2f}" .format (pizza_names[pizza_ordered], pizza_prices[pizza_ordered]))
            num_pizzas = num_pizzas-1





# Print order out - including if order is delivering or pick up and names and price of each pizza - total cost including any delivery charge 
def print_order(del_pick):
    print()
    total_cost = sum(order_cost)
    print ("Customer Details")
    if del_pick == "pickup":
        print("Your order is for Pickup")
        print(f" Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
    elif del_pick == "delivery":  
        print("Your order is for Delivery a $5.00 delivery charge applies")  
        total_cost = total_cost + 5
        print(f" Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Adress:{customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    print()
    print("Your Order Details")
    count = 0
    for item in order_list:
        print( "Ordered: {}  Cost: ${:.2f}" .format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")



# Ability to cancel or proceed with order

def confirm_cancel(): 
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between, {LOW} and {HIGH}")
    print ("Please confirm your order")
    print (" To confirm please enter 1.")
    print (" To cancel please enter 2.")
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print ("Order Confirmed")
        print ("Your order has been sent to our kitchen")
        print ("Your delicious pizza will be with you shortly")
        new_exit()

    elif  confirm == 2:
        print ("Your order has been cancelled")
        print ("You can restart your order or exit the Bot")
        new_exit()
    

# Option for new order or to exit 

def new_exit():
    LOW = 1
    HIGH = 2
    question = (f"Enter a number between, {LOW} and {HIGH}")
    print ("Do you want to start another Order or exit?")
    print ("To start another order enter 1.")
    print ("To exit the Bot enter 2.")
    confirm = val_int(LOW, HIGH, question)
    if confirm == 1:
        print ("New Order")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        main()

    elif  confirm == 2:
        print ("Exit")
        order_list.clear()
        order_cost.clear()
        customer_details.clear()
        sys.exit
  





# Main function 
def main():
    
    """
    Purpose:To run all functions
    Parameters: None 
    Returns: None

    """
    welcome()
    del_pick = order_type()
    menu()
    order_pizza()
    print_order(del_pick)
    confirm_cancel()
    new_exit()

main()