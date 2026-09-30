from customer import customer
from validation import val_name, val_phone
from order import order
from billing import calculate_bill, display_bill

print("********************************************")
print("***********WELCOME TO MAYURI FOODS***********")
print("********************************************")

customer = customer()

customer["name"] = val_name(customer["name"])
customer["phone"] = val_phone(customer["phone"])    

order = order()
subtotal, discount, final = calculate_bill(order)
display_bill(order, subtotal, discount, final)