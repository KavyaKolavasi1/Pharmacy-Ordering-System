
class Menu:
    """ Menu class creates menu items with cost for all available items"""
    def __init__(self, type, style, price):
        """ Initialize the type,style, and price of for each menu item"""
        self._type = type    # refers to the item category (ie, taco, burrito, drink, etc).
        self._style = style  # refers to the menu item name
        self._price = price  # refers to the cost of the menu item

    def get_type(self):
        """ Obtain the type of each menu item"""
        return self._type

    def get_style(self):
        """ Obtain the style of each menu item"""
        return self._style

    def get_price(self):
        """ Obtain the price of each menu item"""
        return self._price

    def __repr__(self):
        """ Visualize contents of the menu object"""
        return f'(\'{self._style}\', {self._price})'

class TacoBell:
    """ TacoBell class adds all items to menu"""
    def __init__(self):
        self._menu = {}  # key = style, value = cost

    def add_to_menu(self, style, cost):
        """ Add each item to menu with cost"""

        # key = style, value = cost
        self._menu[style] = cost

    def get_cost(self, style):
        """ Obtain the individual cost of each item"""

        # return the value, cost
        return self._menu[style]

    def print_menu(self):
        """ Print available menu items"""
        for k, v in self._menu.items():
            print(f"{k} = ${v}")

class Order:
    """ Order class creates a customer with unique order contents"""
    def __init__(self, name):
        """ Initialize variables related to the customer's order"""
        self._customer_name = name
        self._styles = []           # List of items ordered
        self._counts = []           # List of counts for each item ordered

    def customer_order(self, styles, counts):
        """ Create a customer order of item name and counts"""
        self._styles = styles
        self._counts = counts

    def get_customer_name(self):
        """ Return customer name"""
        return self._customer_name

    def compute_order_cost(self, tacobell):
        """ Return the total cost of each customer's order"""

        # Compute cost of this order. Note that to determine the price
        # of a style, Tacobell object reference is passed to this method

        cost = 0
        # Obtain each individual item style with associated cost.
        # Multiply count by individual item price to obtain total cost
        for i in range(len(self._styles)):
            style = self._styles[i]
            count = self._counts[i]
            price = tacobell.get_cost(style)
            item_cost = price * count
            cost += item_cost
        return cost

    def print_customer_order(self,tacobell):
        """ Print the contents of customer's order"""

        # Print the customer name, followed
        # by each item and count

        print(f"{self._customer_name}'s Order:")

        # Loop through ordered items and counts
        # Print the computed costs
        for i in range(len(self._styles)):
            print(self._styles[i], self._counts[i])
        total_cost = self.compute_order_cost(tacobell)
        print(f"Total Cost: ${total_cost}")

class Sales:
    """ Sales class computes sales for day"""
    def __init__(self,name):
        """ Initialize the sales for each customer """

        self._sales = []  # List of item/cost object for each customer
        self._customer_name = name

    def add_order(self, order):
        """ Add each customer's order to sales list"""

        # Order object consists of item and cost of item
        self._sales.append(order)

    def compute_total_sales(self, tacobell):
        """ Compute total sales for the day of all customers"""

        total_sales = 0
        # Loop through sales list of orders
        for order in self._sales:
            # Find individual cost of each item per customer
            order_cost = order.compute_order_cost(tacobell)
            # Compute the total sales for each customer
            total_sales += order_cost
        return total_sales

if __name__ == "__main__":

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


