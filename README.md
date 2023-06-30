
# TacoBell Order System Implementation in Python - README





## Table of Contents


1)  [Overview](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#overview)

2)  [Menu Class](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#menu-class)

3)  [TacoBell Class](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#tacobell-class)

4)  [Order Class](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#order-class)

5)  [Sales Class](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#sales-class)

6) [Output](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#output)

4) [Reflection](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#reflection)


## Overview
This project is the implemention of popular items on the TacoBell menu and a system to capture each customer's order, total cost, as well as total sales for the day using python. Below, I will discuss the use of object oriented programming to create this sytem.


## Menu Class
### Description
The Menu class initializes a new menu item using type, style, and price to define each item available for order.
### Implementation
*  **_ init_(self,type,style,price):** This method initializes the type ((ie, taco, burrito, drink, etc), style (menu item name), price(cost) of each item. All data members are private and can only be called within the player class directly.
* **get_type(self):** This method will return the type of each menu item
* **get_style(self):** This method will return the style of each menu item
* **get_price(self):** This method will return the price of each menu item
* **_repr_(self):** This method will help to visualize the contents of the menu object


## TacoBell Class
### Description
The TacoBell class will add all newly created item objects to the menu.
### Implementation
* **_ init_(self):** This method initializes the menu as a dictionary, with the key being the style and value being cost.
* **add_to_menu(self,style,cost):** This method will add each item object to the menu.
* **get_cost(self,style):** This method will obtain the individual cost for each item.
* **print_menu(self):** This method will print the available menu items.



## Order Class
### Description
The Order class will create a customer and add their unique order (item and counts of each item) into a tacobell order object.
### Implementation
* **_ init_(self,name):** This method initializes a styles list (list of items ordered) and counts list (list of counts of each item) to a customer order. 
* **customer_order(self,styles,counts):** This method will create a customer order of item name and counts
* **get_customer_name(self):** This method will return the customer name.
* **compute_order_cost(self,tacobell):** This method will return the total cost of each customer's order.
* **print_customer_order(self,tacobell):** This method will print the contents of each customer and their order with items and counts.


## Sales Class
### Description
The Sales class will be used to compute the total sales from each customer for the day.
### Implementation
* **_ init_(self,name):** This method initializes a sales list(list of item/cost for each customer) and the customer name.
* **add_order(self):** This method will add the orders of each customer with cost into the sales list.
* **compute_total_sales(self,tacobell):** This method will compute the total sales for the day for all customers.



## Output

### A simple example of how the class can be used below:

    # Create Menu Objects of items and cost
    T1 = Menu("Taco", "Spicy Potato Soft Taco", 2)
    T2 = Menu("Taco", "Crunchy Bean Taco", 2)
    T3 = Menu("Taco", "Soft Bean Taco", 2)
    B1 = Menu("Burrito", "Fiesta Veggie Burrito", 3)
    B2 = Menu("Burrito", "7-layer Burrito", 3)
    P1 = Menu("Pizza", "Mexican Pizza", 4)
    D1 = Menu("Drink", "Coca Cola", 1)
    D2 = Menu("Drink", "Pepsi", 1)
    D3 = Menu("Drink", "Water", 1)

    # Create taco bell object and add each item and price to menu
    tc = TacoBell()
    tc.add_to_menu(T1.get_style(), T1.get_price())
    tc.add_to_menu(T2.get_style(), T2.get_price())
    tc.add_to_menu(T3.get_style(), T3.get_price())
    tc.add_to_menu(B1.get_style(), B1.get_price())
    tc.add_to_menu(P1.get_style(), P1.get_price())
    tc.add_to_menu(D1.get_style(), D1.get_price())
    tc.add_to_menu(D2.get_style(), D2.get_price())
    tc.add_to_menu(D3.get_style(), D3.get_price())

    # Print Menu
    print("\n")
    print("TACO BELL: MENU ITEMS\n")
    tc.print_menu()

    print("\n")
    c1 = Order("Dan")

    c2 = Order("Kim")

    # Important: Be careful to type in item styles and not item type
    c1.customer_order(["Water", "Mexican Pizza"], [1, 2])
    c2.customer_order(["Pepsi", "Soft Bean Taco"], [1, 2])

    # Print Customer order
    c1.print_customer_order(tc)
    print()
    c2.print_customer_order(tc)
    print()

    # Create Sales objects for each customer and add order to sales list
    s1 = Sales("Dan")
    s2 = Sales("Kim")
    s1.add_order(c1)
    s2.add_order(c2)

    sales_list = [s1,s2]

    # Compute the total sales for all customers
    total_profit = 0
    for sales in sales_list:
        total_profit += sales.compute_total_sales(tc)

    # Print the overall total sales
    print(f"Total Sales for Day: ${total_profit}")



### And the output will be:
    TACO BELL: MENU ITEMS
    Spicy Potato Soft Taco = $2
    Crunchy Bean Taco = $2
    Soft Bean Taco = $2
    Fiesta Veggie Burrito = $3
    Mexican Pizza = $4
    Coca Cola = $1
    Pepsi = $1
    Water = $1

    Dan's Order:
    Water 1
    Mexican Pizza 2
    Total Cost: $9

    Kim's Order:
    Pepsi 1
    Soft Bean Taco 2
    Total Cost: $5

    Total Sales for Day: $14

## Reflection
The idea behind this implementation arose because of issues with obtaining order's for multiple people in a friend group or work setting. Items were being regularly missed or orders incorrectly placed due to the large amount of orders being taken by one person. To improve upon this project, I would like to create a mobile app that can be used by others to take a quick survey of orders without having to pass around a phone or bombared with messages of orders. This will help to reduce and make the process more efficient.

