#customer detalis dictionary
customer_details = {}

#Basic instruction 
print("please enter the pickup information")

#customer name not blank
valid = False
while not valid:
    customer_details['name'] = input("please enter your name")
    if customer_details['name'] != "":
        print (customer_details['name'])
        break 

    else:
          print("Sorry this cannot be blank")

#customer phone number not blank 
valid = False 
while not valid:
     customer_details ['phone'] = input("please enter your phone number")
     if customer_details ['phone'] != "":
         print(customer_details ['phone'])

         break
     else:
         print("Sorry this cannot be blank")
