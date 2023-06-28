
# TacoBell Order System Implementation in Python - README





## Table of Contents

1)  [Overview](https://github.com/KavyaKolavasi1/Mancala#overview)

2)  [Menu Class](https://github.com/KavyaKolavasi1/Mancala#player-class)

3)  [TacoBelll Class](https://github.com/KavyaKolavasi1/Mancala#mancala-class)

4) [Output](https://github.com/KavyaKolavasi1/Mancala#output)

4) [Reflection](https://github.com/KavyaKolavasi1/Mancala#reflection)


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



        
## Output

### A simple example of how the class can be used below:





### And the output will be:




## Reflection

As a child my brother and I would always play mancala year round and would even have family tournaments, thus this board game holds a special place in my heart. This implementation using python, introduces the concepts of object oriented programming which focuses on using classes and objects to represent data and create larger programs such as this. This program is a text based version of the game with two players.
