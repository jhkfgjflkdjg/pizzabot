#list of pizza names
pizza_names = ['Margherita','Pepperoni','Hawaiian','Cheese ','Italian','Veggie','Vegan','Chicken Deluxe',
                'Mega Meat Lovers','Seafood Deluxe','Apricot chicken Deluxe','BBQ Chicken Deluxe']
#List of pizza prices  
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

#List to store orderd pizzas 
order_list=[]
#List to store pizzas prices    
order_cost=[]

#List to store order cost 

def menu():
    number_pizza = 12

    for count in range (number_pizza):
        print("{} {} ${:.2f}" .format(count+1,pizza_names[count],pizza_prices[count]))

menu()  

# ask for total number of pizza for order
num_pizzas = 0

num_pizzas = int(input("How many pizza do you want to order? "))

print(num_pizzas)

#choose pizza from menu 
print("please choose your pizzas by entering the numeber from the menu")
for item in range(num_pizzas):
    while num_pizzas > 0:
        pizza_orderd = int(input())
        pizza_orderd = pizza_names -1
        order_list.append(pizza_names[pizza_orderd])
        order_cost.append(pizza_prices[pizza_orderd])
        print("{} {} ${:.2f}" .format(pizza_names[pizza_orderd],pizza_prices[pizza_orderd]))
        num_pizzas = num_pizzas -1 




    







#count down until all pizzas are ordered 



#print order