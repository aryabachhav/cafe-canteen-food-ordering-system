from data import menu

def calculate_bill(order):
    subtotal = 0

    for item_id, qty in order.items():
        price = menu[item_id]["price"]
        subtotal = subtotal + (price * qty)

    if subtotal >= 500: discount_rate = 15
    elif subtotal >= 300: discount_rate = 10
    elif subtotal >= 200: discount_rate = 5
    else: discount_rate = 0

    discount = subtotal * discount_rate / 100
    final_amount = subtotal - discount

    return subtotal, discount, final_amount 


def display_bill(order, subtotal, discount, final_amount):
    print("\n********** ORDER SUMMARY **********")
    print("Item\t\t\tQty\tPrice\tTotal")
    print("*********************************************")

    for item_id, qty in order.items():
        name = menu[item_id]["name"]
        price = menu[item_id]["price"]
        total = price * qty
        print(name,"\t\t",qty,"\t", price,"\t", total)

    print("*********************************************")
    print("Subtotal:      ₹", subtotal)
    print("Discount:      ₹", discount)
    print("Final Amount:  ₹", final_amount)