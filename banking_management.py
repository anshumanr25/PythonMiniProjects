# Python Banking Program

def show_balance(balance):
    print(f"Your current balance is {balance:.2f}/-.")

def deposit():
    amount = float(input("Enter the amount to be deposited: "))

    if amount < 0:
        print("That's not a valid amount.")
        return 0
    else:
        return amount


def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than zero")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*****************************************")
        print("     Welcome to XYZ Bank..!!!    ")
        print("*****************************************")
        print("Please choose from below services:")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Please enter a valid choice.")

    print("Thank you for visiting...\nHave a nice day.....")

if __name__ == '__main__':
    main()