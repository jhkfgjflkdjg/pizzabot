print("Do you want to start another Order or Exit")
print ("To start another order enter 1")
print ("To exit the BOT enter 2")
while True:
    try: 
     Confirm = int(input("please enter a number"))
     if Confirm >= 1 and Confirm <= 2:  
        if Confirm == 1:
            print ("New Order")
            break 
         
        elif Confirm == 2:
            print ("Exit")
            break 
     else:
         print ("Number must be 1 or 2")
    except ValueError:
      print("That is not a valid number")
      print("please enter 1 or 2")