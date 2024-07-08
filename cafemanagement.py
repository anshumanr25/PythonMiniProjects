menu = {
    "Pizza": 50,
    "Burger": 80,
    "Pasta": 50,
    "Coffee": 80,
    "Chai": 25
}


def greetings():
    print("Namaste\nWelcome to PYTHON Cafe!!!")


greetings()

# menu
print("Menu:")
for key, val in menu.items():
    print(f"{key} : {val}/-")

# order
total_order = 0
item1 = input("Please select your order from the menu : ").capitalize()
item1_qnt = int(input("Please enter the quantity for the above order : "))

# order calculation
if item1 in menu:
    total_order += (menu[item1] * item1_qnt)
    print(f"Your order for {item1_qnt} * {item1} has been successfully placed.")
else:
    print("Please select from the menu only...")
    print(f"The ordered item {item1} is not present in our menu.")

# another order
while True:
    another_order = input("Do you want to order any other item? (yes/no) : ")
    if another_order.lower() == "yes":
        item2 = input("Please enter your order : ").capitalize()
        item2_qnt = int(input("Please enter the quantity for the above order : "))

        if item2 in menu:
            total_order += (menu[item2] * item2_qnt)
            print(f"Your order for {item2_qnt} * {item2} has been successfully placed.")
        else:
            print("Please select from the menu only...")
            print(f"The ordered item {item2} is not present in our menu.")
    else:
        break

print(f"The total amount to pay for your order is {total_order}Rs/-")
print("Thank you for visiting our cafe!!!")
