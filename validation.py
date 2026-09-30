def val_name(name):
    while name == "":
        print("Name cannot be empty.")
        name = input("Enter customer name:")
    return name


def val_phone(phone):
    while len(phone)!=10 or not phone.isdigit():
        print("Please enter a valid 10-digit phone number.")
        phone = input("Enter phone number:")
    return phone


def val_qty(qty):
    while not qty.isdigit() or int(qty) <= 0:
        print("qty must be a positive number.")
        qty = input("Enter qty:")
    return int(qty)

def val_item_id(item_id, menu):
    while not item_id.isdigit() or (int(item_id) not in menu):
        print("Invalid item ID.")
        item_id = input("Enter a valid item ID:")
    return int(item_id)