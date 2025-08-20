balance = 0
qtdDeposit = 0
qtdWithdrawal = 0
WITHDRAWAL_LIMIT = 3
code = 'a'
stratment = ''

name = input("Hi! What is your name?\n")

while (code!= 'q'):
    code = input(f"""
Hi {name.title()}, welcome to service of Center Bank!
                 
Your balance: ${balance}

Type a letter to choose the operation:
[d] Deposit
[w] Withdrawal
[s] Stratament
[q] Quit

=> """)

    if (code == 'd'): #quando o usuário quer depositar
        deposit = float(input("Enter a value: $"))

        if (deposit <= 0):
            while (deposit <= 0):
                print("Value invalid, try again")
                deposit = float(input("Enter a value: $"))
        else:
            balance += deposit
            qtdDeposit += 1
            stratment += f"\nDeposit: ${deposit:.2f}"

            print("\nDeposit sucessfull!")
            print(f"New balance: {balance}\n--------------------------------------------------")

    elif (code == 'w'): #quando o usuário quer sacar
        if (qtdWithdrawal >= WITHDRAWAL_LIMIT):
            print("\n*** You have reached the daily withdrawal limit ***")

        else:
            withdrawal = float(input("Enter an amount to withdrawal (The withdrawal limit is 500): $"))

            if (withdrawal > balance): #se o saque for maior que o saldo atual
                while (withdrawal < 0 or withdrawal > 500 or withdrawal > balance):
                    if (withdrawal < 0):
                        print("Value invalid, try again!")
                        withdrawal = float(input("Enter an amount to withdrawal (The withdrawal have positive): $"))
                    elif (float(withdrawal) > 500):
                        print("You have exceeded the maximum withdrawal amount, try again!")
                        withdrawal = float(input("The withdrawal must be less than 500!\nEnter an amount to withdrawal: $"))
                    elif (float(withdrawal) > balance):
                        print("The withdrawal must be small than the balance!")
                        withdrawal = float(input("Enter other amount to withdrawal: $"))

            elif (withdrawal <= 0): #se o saque for negativo
                while (withdrawal < 0 or withdrawal > 500 or withdrawal > balance):
                    if (withdrawal < 0):
                        print("Value invalid, try again!")
                        withdrawal = float(input("Enter an amount to withdrawal (The withdrawal have positive): $"))
                    elif (withdrawal > 500):
                        print("You have exceeded the maximum withdrawal amount, try again!")
                        withdrawal = float(input("The withdrawal must be less than 500!\nEnter an amount to withdrawal: $"))
                    elif (withdrawal > balance):
                        print("The withdrawal must be small than the balance!")
                        withdrawal = float(input("Enter other amount to withdrawal: $"))

            elif (withdrawal > 500): #se o saque for maior que 500
                while (withdrawal < 0 or withdrawal > 500 or withdrawal > balance):
                    if (withdrawal < 0):
                        print("Value invalid, try again!")
                        withdrawal = float(input("Enter an amount to withdrawal (The withdrawal have positive): $"))
                    elif (withdrawal > 500):
                        print("You have exceeded the maximum withdrawal amount, try again!")
                        withdrawal = float(input("The withdrawal must be less than 500!\nEnter an amount to withdrawal: $"))
                    elif (withdrawal > balance):
                        print("The withdrawal must be small than the balance!")
                        withdrawal = float(input("Enter other amount to withdrawal: $"))
        
            balance -= withdrawal
            qtdWithdrawal += 1
            stratment += f"\nWithdrawal amount: ${withdrawal:.2f}"
            print(f"\nWithdrawal sucessfull\nNew balance: {balance}\n--------------------------------------------------\n")
    
    elif (code == 's'): #incrementar extratos quando saque e depósito forem bem sucedidos
        if (stratment == ''):
            print("There have not been any transactions yet!")
        else:
            print(f"""{stratment}
Quantity of deposit: {qtdDeposit}
Quantity of withdrawal: {qtdWithdrawal}
Actualy balance: ${balance:.2f}
""")

    else: #quando usuário digita letra não correspondente
        if (code == 'q'):
            print("The central bank thanks you, see you next time!")
        else:
            print("\nInvalid operation, please select a correct letter!")