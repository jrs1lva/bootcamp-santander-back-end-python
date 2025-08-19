balance = 0
qtdDeposit = 0
qtdWithdrawal = 0
code = 'a'
name = input("Hi! What is your name?\n")

while ( code!= 'q'):
    code = input(f"""\nHi {name.title()}, welcome to service of Center Bank
    Your balance: {balance}

    Type a letter to choose the operation:
    [d] Deposit
    [w] Withdrawal
    [s] Stratament
    [q] Quit
    """)

    if (code == 'd'):
        deposit = input("Enter a value: ")

        if (float(deposit) <= 0):
            while (float(deposit) <= 0):
                print("Value invalid, try again")
                deposit = input("Enter a value:")
        else:
            balance += float(deposit)
            qtdDeposit += 1
            print("\nDeposit sucessfull!")
            print(f"New balance: {balance}\n--------------------------------------------------\n")

    elif (code == 'w'):
        if (qtdWithdrawal > 3):
            print("\n*** You have reached the daily withdrawal limit ***")

        else:
            withdrawal = input("Enter an amount to withdrawal (The withdrawal limit is 500): ")

            if (float(withdrawal) < 0):
                while (float(withdrawal) < 0 or float(withdrawal) > 500):
                    if (float(withdrawal) < 0):
                        print("Value invalid, try again!")
                        withdrawal = input("Enter an amount to withdrawal (The withdrawal have positive): ")
                    elif (float(withdrawal) > 500):
                        print("You have exceeded the maximum withdrawal amount, try again!")
                        withdrawal = input("The withdrawal must be less than 500!\nEnter an amount to withdrawal: ")

            elif (float(withdrawal) > 500):
                while (float(withdrawal) < 0 or float(withdrawal) > 500):
                    if (float(withdrawal) < 0):
                        print("Value invalid, try again!")
                        withdrawal = input("Enter an amount to withdrawal (The withdrawal have positive): ")
                    elif (float(withdrawal) > 500):
                        print("You have exceeded the maximum withdrawal amount, try again!")
                        withdrawal = input("The withdrawal must be less than 500!\nEnter an amount to withdrawal: ")
        
            balance -= float(withdrawal)
            qtdWithdrawal += 1
            print(f"\nWithdrawal sucessfull\nNew balance: {balance}\n--------------------------------------------------\n")
    
    if (code)
print("The central bank thanks you, see you next time!")