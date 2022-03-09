#List to store orderd pizzas 
order_list=['Margherita','Hawaiian','Vegan','Chicken Deluxe']
#List to store pizzas prices    
order_cost=[8.50,8.50,8.50,13.50]

cust_details = {'name': 'Jodek','phone': '02123424','house': '23', 'street': 'Burry','suburb': 'Howick'}

def print_order():
    total_cost = sum(order_cost)
    print("Customer_Details")
    print(f"Customer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    print()
    print("Order Deatils")
    count= 0  
    for item in order_list:
        print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")

    print_order()