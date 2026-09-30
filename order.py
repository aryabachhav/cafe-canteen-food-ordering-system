from data import menu
from menu import display
from validation import val_item_id, val_qty

def order():
    order = {}
    while True: 
        display()
        item_id = input("Enter item ID:")
        item_id = val_item_id(item_id, menu)

        qty = input("Enter qty:")
        qty = val_qty(qty) 

        if item_id in order:  order[item_id] = order[item_id] + qty
        else: order[item_id] = qty

        print(qty, "x", menu[item_id]["name"], "added to your order.")

        choice = input("Do you want to add another item? y/n ")
        if choice.lower()=='n':break

    return order