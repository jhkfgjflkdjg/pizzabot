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



def main():
    ''' 
    Purpose: To run all fuctions 
    a welcome message 
    parameter: None
    Returns: None
    '''
    welcome()


main ()

