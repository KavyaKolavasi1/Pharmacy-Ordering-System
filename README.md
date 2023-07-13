
# Pharmacy Order System Implementation in Python - README





## Table of Contents


1)  [Overview](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#overview)

2)  [Catalog Class](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#menu-class)

3)  [Pharmacy Class](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#tacobell-class)

4)  [Order Class](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#order-class)

5)  [Sales Class](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#sales-class)

6) [Output](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#output)

4) [Reflection](https://github.com/KavyaKolavasi1/TacoBell-Ordering-System#reflection)


## Overview
This project is the implemention of popular medications in our pharmacy catalog and a system to capture each customer's order, total cost, as well as total sales for the day using python. On a day to day I take many medication orders from doctors and patients, and having a system to quickly document these orders and calulate a cost and total sales is very beneficial. It reduces the amount of time necessary to input orders while I create prescriptions. Below, I will discuss the use of object oriented programming to create this sytem. 

#### The items and costs entered here are not reflective of the actual costs associated at my pharmacy workplace. I have a personal copy I utilize in my day to day that I am not able to publish due to non-disclosure. The below program is a sample.

#### This was originally a TacoBell ordering system but was altered to a pharmacy system to assist my day to day needs.


## Pharmacy Class
### Description
The Pharmacy class initializes a new medication item using category, medication name, and price to define each item available for order.
### Implementation
*  **_ init_(self,cateogry,medication,price):** This method initializes the category ((ie, derm, weight loss, hormone, etc), medication (item name), price(cost) of each item. All data members are private and can only be called within the player class directly.
* **get_category(self):** This method will return the category of each item
* **get_medication(self):** This method will return the medication of each item
* **get_price(self):** This method will return the price of each item
* **_repr_(self):** This method will help to visualize the contents of the catalog object


## Pharmacy Class
### Description
The Pharmacy class will add all newly created medication objects to the catalog.
### Implementation
* **_ init_(self):** This method initializes the catalog as a dictionary, with the key being the medication and value being cost.
* **add_to_catalog(self,medication,cost):** This method will add each medication to the catalog.
* **get_cost(self,medication):** This method will obtain the individual cost for each item.
* **print_catalog(self):** This method will print the available catalog items.



## Order Class
### Description
The Order class will create a customer and add their unique order (medication and counts of each item) into a pharmacy order object.
### Implementation
* **_ init_(self,name):** This method initializes a medications list (list of items ordered) and counts list (list of counts of each item) to a customer order. 
* **customer_order(self,medications,counts):** This method will create a customer order of medication name and counts
* **get_customer_name(self):** This method will return the customer name.
* **compute_order_cost(self,pharmacy):** This method will return the total cost of each customer's order.
* **print_customer_order(self,pharmacy):** This method will print the contents of each customer and their order with medication and counts.


## Sales Class
### Description
The Sales class will be used to compute the total sales from each customer for the day.
### Implementation
* **_ init_(self,name):** This method initializes a sales list(list of item/cost for each customer) and the customer name.
* **add_order(self):** This method will add the orders of each customer with cost into the sales list.
* **compute_total_sales(self,pharmacy):** This method will compute the total sales for the day for all customers.



## Output

### A simple example of how the class can be used below:

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



### And the output will be:
    Pharmacy: CATALOG ITEMS
    Melasma Cream = $50
    Hair Restoration Solution = $50
    Rosacea Cream = $50
    Semaglutide = $100
    Phentermine = $0.5
    Lipo Caps = $1
    Testosterone Injection = $45
    Progesterone Cream = $20
    Estradiol Cream = $20
    
    
    Dan's Order:
    Melasma Cream 1
    Phentermine 30
    Total Cost: $65.0
    
    Kim's Order:
    Progesterone Cream 1
    Semaglutide 2
    Total Cost: $220
    
    Total Sales for the Day: $285.0

## Reflection
The idea behind this implementation arose because of issues with taking down prescription orders quickly and display a cost. Many times a customer will want to know the total and individual costs of their medications and unfortunatley our system does not give this information until all the medication order's are already inputted into the system. Therefore having this ability greatly reduces the time to calculate this information. This is also useful because I can quickly record the orders of a patient and input into our system after the phone conversation is completed. To improve upon this project, I would like to create a mobile app that can be used by others to take a quick survey of orders. This will help to reduce and make the process more efficient.

