identity = input("Are You a customer or shopkeeper?: ")

default_items = {"rice": {"price": 60, "count": 30}, "wheat": {"price": 20, "count": 30}, "sugar": {"price": 40, "count": 70}, "ghee": {"price": 600, "count": 40}, "soap": {"price": 30, "count": 100}, "toothpaste": {"price": 50, "count": 80}}
items_length = len(default_items)
your_list = {}

def buy():
    product = input("What do you want to buy?: ")
    if product in default_items:
        quantity = int(input("How much?: "))
        default_items[product]["count"] -= quantity
        print(default_items)
        your_list[product] = default_items[product]["price"] * quantity
        print(your_list)
    else:
        print("Product not available")

def bill():
    total = sum(your_list.values())
    if (total > 500) and (total < 1000):
        discount = total * 5 / 100
        total -= discount
        print("Your Bill is Rs", total)
    elif total > 1000:
        discount = total * 10 / 100
        total -= discount
        print("Your Bill is Rs", total)
    else:
        print("Your Bill is Rs", total)

def stock_management():
    item = input("Name of Item: ")
    price = int(input("Cost of Item?: "))
    count = int(input("Quantity of Item?: "))
    default_items[item] = {"price": price, "count": count}
    print(default_items)

if identity == "customer":
    print(default_items)
    choice = input("Enter 'p' for Purchase or 'b' for Bill: ")
    for i in range(items_length):
        if choice == "p":
            buy()
            choice = input("Enter 'p' for Purchase or 'b' for Bill: ")
            if choice == "b":
                bill()
elif identity == "shopkeeper":
    work = input("Do you want to see Stock 's' or Add Items 'i' in store?: ")
    for i in range(items_length):
        if work == "s":
            print(default_items)
            work = input("Do you want to see Stock 's' or Add Items 'i' in store?: ")
        elif work == "i":
            stock_management()
            work = input("Do you want to see Stock 's' or Add Items 'i' in store?: ")


