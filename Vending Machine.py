print("""
██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝
""")
print("""==========================(DRINKS)==============================
==     Item: Water. price : 1.00                 A1           ==
==     Item: Soda.  price : 3.00                 A2           ==
==     Item: Lipton Iced Tea.  price : 5.00      B1           ==
==     Item: Strawberry milk.  price : 3.00      B2           ==
==     Item: Chocolate milk.   price : 3.00      B3           ==
==     Item: Orange juice.     price : 2.00      C1           ==
==     Item: Berry juice.      price : 2.00      C2           ==
==========================(SNACKS)==============================
==     Item: Small Chips. price : 3.00           C3           ==
==     Item: Croissant.   price : 4.00           C4           ==
==     Item: M&M.         price : 3.00           D1           ==
==     Item: Snickers.    price : 2.50           D2           ==
==     Item: Chicken puff. price : 5.00          D3           ==
==     Item: Hotdog.      price : 4.00           D4           ==
==     Item: Oreos.       price : 2.50           D5           ==
================================================================""")

# Menu
item = {
    "A1": {'name': 'Water', 'price': 1.00},
    "A2": {'name': 'Soda', 'price': 3.00},
    "B1": {'name': 'Lipton Iced Tea', 'price': 5.00},
    "B2": {'name': 'Strawberry milk', 'price': 3.00},
    "B3": {'name': 'Chocolate milk', 'price': 3.00},
    "C1": {'name': 'Orange juice', 'price': 2.00},
    "C2": {'name': 'Berry juice', 'price': 2.00},
    "C3": {'name': 'Samll CHips', 'price': 3.00},
    "C4": {'name': 'Croissant', 'price': 4.00},
    "D1": {'name': 'M&M', 'price': 3.00},
    "D2": {'name': 'Snickers', 'price': 2.50},
    "D3": {'name': 'Chicken puff', 'price': 5.00},
    "D4": {'name': 'Hotdog', 'price': 4.00},
    "D5": {'name': 'Oreos', 'price': 2.50}
}

print("Welcome to Kurt's Vending machine.")

object = str(input("So tell me, what are you buying?: "))

# Confirm item
if object in item:
    selected_item = item[object]
    print("====================================")
    print(f"You have selected {selected_item['name']}.")
    print("====================================")
    amount = selected_item['price']

    # Money Payment
    while amount > 0:
        payment = float(input(f"Please insert amount ${amount:.2f}: "))
        if payment >= amount:
            change = payment - amount
            print("====================================")
            print(f"You have purchased {selected_item['name']}!")
            print("====================================")
            print(f"Thank you for your purchase! Your change is ${change:.2f}")
            break
        else:
            print("Insufficient payment. Please insert more.")
            amount -= payment
else:
    print("That's not in my shop. Please enter given selection.")