# pizza bot program
import random
from random import randint 

# List of random names 
names =["Mikara","Jodek","Tomas","Carlos","Karlo","Louis","Joaquin","Shawn","Marcus","Gabe"]

def welcome():
    ''' 
    Purpose: To generate a random name from the list and print out 
    a welcome name 
    parameter: None
    Returns: None
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to Dream Pizza***")
    print("*** My name is",name, "***")
    print("*** I will be here to help you order your delicious Dream Pizza***")

  #main for pickup and delivery 

def pickup(): 
 print ("Is your order for pickup or delivery?")

print ("For pickup please enter 1")
print ("For delivery please enter 2")
while True:
    try: 
     delivery = int(input("please enter a number"))
     if delivery >= 1 and delivery <= 2:  
        if delivery == 2:
            print ("Delivery")
            break 
        
        elif delivery == 1:
            print ("Pickup")
            break 
     else:
         print ("Number must be 1 or 2")
    except ValueError:
      print("That is not a valid number")
      print("please enter 1 or 2")

#pick up information- name and phone number 




# Delivery information - name address and phone



#choose total number of Pizzas - max 5



# pizza menu 




# Pizza order - from menu - print each pizza ordered with cast









# main fuction 
def main():   
    ''' 
    Purpose: To run all fuctions 
    a welcome message 
    parameter: None
    Returns: None
    '''
    welcome()
    pickup()
    

main ()