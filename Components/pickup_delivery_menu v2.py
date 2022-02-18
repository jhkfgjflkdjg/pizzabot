# Bugs 
# will only work for vaild input "d" and "p"
#invaild input triggers else statment but program does not as for input agian 

# menu so that user can choose either pickup or delivery 

print ("Do you want your order delivered or are you picking it up?")

print ("For delivery enter d")
print ("For pickup enter p")

delivery = input()

if delivery == "d":
    print ("Delivery")

elif delivery == "p":
    print ("Pickup")

else:
    print ("That was not a vaild input")