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
        withdrawal = input("Enter withdrawal amount: ")

        while (float(withdrawal) <= 0 or float(withdrawal) > balance):
            if (float(withdrawal) <= 0):
                print("Value invalid, try again.")
                withdrawal = input("Enter withdrawal amount: ")

            elif (float(withdrawal) > balance):
                print("Insufficient balance, try again.")
                withdrawal = input("Enter withdrawal amount: ")

        balance -= float(withdrawal)
        print("Withdrawal sucessfull!")
        print(f"Your new balance: {balance}$")
    else:
        print("Invalid option, try again.")
        
    print("Thank you for using Center Bank!")
    code = input("Type -1 to exit or any other number to continue.")

print("See you next time!")