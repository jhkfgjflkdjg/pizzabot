# menu so that user can choose either pickup or delivery 

#Bug - need to make it so that it only accepts 1 or 2 

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
      print("please enter 1 or 2)")