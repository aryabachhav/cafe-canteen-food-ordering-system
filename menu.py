from data import menu
def display():
    print("\n*****************************************CANTEEN MENU*****************************************")
    print("ID \t Item \t\t\t\t Category \t Price")
    print("************************************************************************************************")
    for value, key in menu.items():
        print(value, "\t", key["name"], "\t\t", key["category"], "\t", key["price"])