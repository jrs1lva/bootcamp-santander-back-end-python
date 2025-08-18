balance = 0.0
code = 0
name = input("Type your name: ")
while (float(code)!= -1):

    code = input(f"""Hi {name.title()}, welcome to Center Bank.
    Your balance: {balance}$
    Type a number to choose the operation:
    1- Deposit
    2- Withdraw
    """)

    if (float(code) == 1) :
        deposit = input("Enter deposit amount: ")
        while (float(deposit) < 0):
            print("Value invalid, try again.")
            deposit = input("Enter deposit amount:\nEnter -1 to exit:")

        if (float(deposit) > 0):
            balance += float(deposit)
            print(f"Your new balance: {balance}$")

    elif (float(code) == 2):
        withdraw = input("Enter withdraw amount: ")

        while (float(withdraw) <= 0 or float(withdraw) > balance):
            if (float(withdraw) <= 0):
                print("Value invalid, try again.")
                withdraw = input("Enter withdraw amount: ")

            elif (float(withdraw) > balance):
                print("Insufficient balance, try again.")
                withdraw = input("Enter withdraw amount: ")

        balance -= float(withdraw)
        print("Withdraw sucessfull!")
        print(f"Your new balance: {balance}$")
    else:
        print("Invalid option, try again.")
        
    print("Thank you for using Center Bank!")
    code = input("Type -1 to exit or any other number to continue.")

print("See you next time!")