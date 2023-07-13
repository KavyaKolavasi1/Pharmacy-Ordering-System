class Catalog:
    """Catalog class creates catalog with cost for all available medications"""
    def __init__(self, category, medication, price):
        """Initialize the category, mediation, and price for each medication item"""
        self._category = category  # refers to the item category (e.g., dermatology, weight-loss, hormone, etc)
        self._medication = medication  # refers to the medication name
        self._price = price  # refers to the cost of the medication

    def get_category(self):
        """Obtain the category of each item"""
        return self._category

    def get_medication(self):
        """Obtain the medication of each item"""
        return self._medication

    def get_price(self):
        """Obtain the price of each item"""
        return self._price

    def __repr__(self):
        """Visualize the contents of the catalog object"""
        return f'(\'{self._medication}\', {self._price})'


class Pharmacy:
    """Pharmacy class adds all items to the catalog"""
    def __init__(self):
        self._catalog = {}  # key = medication, value = cost

    def add_to_catalog(self, medication, cost):
        """Add each item to the catalog with cost"""
        self._catalog[medication] = cost

    def get_cost(self, medication):
        """Obtain the individual cost of each item"""
        return self._catalog[medication]

    def print_catalog(self):
        """Print available catalog items"""
        for k, v in self._catalog.items():
            print(f"{k} = ${v}")


class Order:
    """Order class creates a customer with unique order contents"""
    def __init__(self, name):
        """Initialize variables related to the customer's order"""
        self._customer_name = name
        self._medications = []  # List of medications ordered
        self._counts = []  # List of counts for each item ordered

    def customer_order(self, medications, counts):
        """Create a customer order of item name and counts"""
        self._medications = medications
        self._counts = counts

    def get_customer_name(self):
        """Return customer name"""
        return self._customer_name

    def compute_order_cost(self, pharmacy):
        """Return the total cost of each customer's order"""
        cost = 0
        # Obtain each individual medication with associated cost.
        # Multiply count by medication price to obtain the total cost
        for i in range(len(self._medications)):
            medication = self._medications[i]
            count = self._counts[i]
            price = pharmacy.get_cost(medication)
            item_cost = price * count
            cost += item_cost
        return cost

    def print_customer_order(self, pharmacy):
        """Print the contents of the customer's order"""
        print(f"{self._customer_name}'s Order:")
        # Loop through ordered medications and counts
        # Print the computed costs
        for i in range(len(self._medications)):
            print(self._medications[i], self._counts[i])
        total_cost = self.compute_order_cost(pharmacy)
        print(f"Total Cost: ${total_cost}")


class Sales:
    """Sales class computes sales for the day"""
    def __init__(self, name):
        """Initialize the sales for each customer"""
        self._sales = []  # List of medication/cost object for each customer
        self._customer_name = name

    def add_order(self, order):
        """Add each customer's order to the sales list"""
        self._sales.append(order)

    def compute_total_sales(self, pharmacy):
        """Compute total sales for the day of all customers"""
        total_sales = 0
        # Loop through sales list of orders
        for order in self._sales:
            # Find the individual cost of each item per customer
            order_cost = order.compute_order_cost(pharmacy)
            # Compute the total sales for each customer
            total_sales += order_cost
        return total_sales


if __name__ == "__main__":
    # Create Catalog Objects of items and cost
    T1 = Catalog("Derm", "Melasma Cream", 50)
    T2 = Catalog("Derm", "Hair Restoration Solution", 50)
    T3 = Catalog("Derm", "Rosacea Cream", 50)
    B1 = Catalog("Weight_Loss", "Semaglutide", 100)
    B2 = Catalog("Weight_Loss", "Phentermine", 0.50)
    P1 = Catalog("Weight_Loss", "Lipo Caps", 1)
    D1 = Catalog("Hormone", "Testosterone Injection", 45)
    D2 = Catalog("Hormone", "Progesterone Cream", 20)
    D3 = Catalog("Hormone", "Estradiol Cream", 20)

    # Create a pharmacy object and add each medication and price to the catalog
    tc = Pharmacy()
    tc.add_to_catalog(T1.get_medication(), T1.get_price())
    tc.add_to_catalog(T2.get_medication(), T2.get_price())
    tc.add_to_catalog(T3.get_medication(), T3.get_price())
    tc.add_to_catalog(B1.get_medication(), B1.get_price())
    tc.add_to_catalog(B2.get_medication(), B2.get_price())
    tc.add_to_catalog(P1.get_medication(), P1.get_price())
    tc.add_to_catalog(D1.get_medication(), D1.get_price())
    tc.add_to_catalog(D2.get_medication(), D2.get_price())
    tc.add_to_catalog(D3.get_medication(), D3.get_price())

    # Print the catalog
    print("\n")
    print("Pharmacy: CATALOG ITEMS\n")
    tc.print_catalog()
    print("\n")

    c1 = Order("Dan")
    c2 = Order("Kim")

    # Important: Be careful to type in medication names and not item category
    c1.customer_order(["Melasma Cream", "Phentermine"], [1, 30])
    c2.customer_order(["Progesterone Cream", "Semaglutide"], [1, 2])

    # Print each customer's order
    c1.print_customer_order(tc)
    print()
    c2.print_customer_order(tc)
    print()

    # Create sales objects for each customer and add their orders to the sales list
    s1 = Sales("Dan")
    s2 = Sales("Kim")
    s1.add_order(c1)
    s2.add_order(c2)

    sales_list = [s1, s2]

    # Compute the total sales for all customers
    total_profit = 0
    for sales in sales_list:
        total_profit += sales.compute_total_sales(tc)

    # Print the overall total sales
    print(f"Total Sales for the Day: ${total_profit}")