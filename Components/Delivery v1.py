#customer detalis dictionary
customer_details = {}




def not_blank(question):
    valid = False 
    while not valid:
        response = input(question)
        if response != "":
            return response. title()
        else:
            print("This cannot be blank")


#Basic instruction 
question = ("please enter your name ")
customer_details['name'] = not_blank(question )
print (customer_details['name']) 
    
question = ("please enter your phone number ")
customer_details ['phone'] = not_blank(question )
print (customer_details['phone'])

question = ("please enter your house number ")
customer_details ['house'] = not_blank(question )
print (customer_details['house'])

question = ("please enter your street name")
customer_details ['street'] = not_blank(question )
print (customer_details['street'])

question = ("please enter your suburb")
customer_details ['suburb'] = not_blank(question )
print (customer_details['suburb'])