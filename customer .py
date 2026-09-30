def customer():
    print("**********CUSTOMER DETAILS**********")
    name = input("Enter your name:")
    phone = input("Enter your phone number:")
    customer = {"name":name, "phone":phone}
    return customer