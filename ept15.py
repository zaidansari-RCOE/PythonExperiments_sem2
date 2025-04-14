'''
Title: Using a Python Debugger
Name: Md. Zaid Mashooque Ansari
Division: C
UIN: 241P057
Roll no: 51
'''

import pdb

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        """Add an item to the shopping cart."""
        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def calculate_total(self):
        """Calculate total price of all items in the cart."""
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']  # Intentional error: what if price is a string?
        return total

def main():
    cart = ShoppingCart()
    
    # Adding items to the cart
    cart.add_item("Laptop", "1000", 1)  # Bug: Price is a string instead of an integer
    cart.add_item("Mouse", 50, 2)
    cart.add_item("Keyboard", 75, 1)

    # Set a breakpoint before calculating total
    pdb.set_trace()

    total_price = cart.calculate_total()
    print("Total Price:", total_price)

if __name__ == "__main__":
    main()

"""
Sample Output:

(Pdb) p cart.items
[{'name': 'Laptop', 'price': '1000', 'quantity': 1}, {'name': 'Mouse', 'price': 50, 'quantity': 2}, {'name': 'Keyboard', 'price': 75, 'quantity': 1}]
(Pdb) p type(cart.items[0]['price'])
<class 'str'>
(Pdb) s
(Pdb) p item['price']
'1000'
(Pdb) p cart.items[1]['price']
50
Error: TypeError: can't multiply sequence by non-int of type 'str'

After fixing the bug by modifying add_item() to ensure price is an integer:
def add_item(self, name, price, quantity):
    self.items.append({'name': name, 'price': int(price), 'quantity': quantity})

Sample Output after Fixing the Bug:

Total Price: 1200
"""
