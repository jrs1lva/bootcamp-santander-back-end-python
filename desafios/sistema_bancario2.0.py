balance = 0
qtdDeposit = 0
qtdWithdrawal = 0
code = 'a'

name = input("Hi! What is your name?\n")

while (code!= 'q'):
    code = input(f"""
Hi {name.title()}, welcome to service of Center Bank!
                 
Your balance: {balance}

Type a letter to choose the operation:
[d] Deposit
[w] Withdrawal
[s] Stratament
[q] Quit
\n""")

    if (code == 'd'): #quando o usuário quer depositar
        deposit = input("Enter a value: ")

        if (float(deposit) <= 0):
            while (float(deposit) <= 0):
                print("Value invalid, try again")
                deposit = input("Enter a value:")
        else:
            balance += float(deposit)
            qtdDeposit += 1

            #incrementar extrato ***********************************************

            print("\nDeposit sucessfull!")
            print(f"New balance: {balance}\n--------------------------------------------------\n")

    elif (code == 'w'): #quando o usuário quer sacar
        if (qtdWithdrawal > 3):
            print("\n*** You have reached the daily withdrawal limit ***")

        else:
            withdrawal = input("Enter an amount to withdrawal (The withdrawal limit is 500): ")

            if (float(withdrawal) > balance): #se o saque for maior que o saldo atual
                while (float(withdrawal) < 0 or float(withdrawal) > 500 or float(withdrawal) > balance):
                    if (float(withdrawal) < 0):
                        print("Value invalid, try again!")
                        withdrawal = input("Enter an amount to withdrawal (The withdrawal have positive): ")
                    elif (float(withdrawal) > 500):
                        print("You have exceeded the maximum withdrawal amount, try again!")
                        withdrawal = input("The withdrawal must be less than 500!\nEnter an amount to withdrawal: ")
                    elif (float(withdrawal) > balance):
                        print("The withdrawal must be small than the balance!")
                        withdrawal = input("Enter other amount to withdrawal:")

            elif (float(withdrawal) <= 0): #se o saque for negativo
                while (float(withdrawal) < 0 or float(withdrawal) > 500 or float(withdrawal) > balance):
                    if (float(withdrawal) < 0):
                        print("Value invalid, try again!")
                        withdrawal = input("Enter an amount to withdrawal (The withdrawal have positive): ")
                    elif (float(withdrawal) > 500):
                        print("You have exceeded the maximum withdrawal amount, try again!")
                        withdrawal = input("The withdrawal must be less than 500!\nEnter an amount to withdrawal: ")
                    elif (float(withdrawal) > balance):
                        print("The withdrawal must be small than the balance!")
                        withdrawal = input("Enter other amount to withdrawal:")

            elif (float(withdrawal) > 500): #se o saque for maior que 500
                while (float(withdrawal) < 0 or float(withdrawal) > 500 or float(withdrawal) > balance):
                    if (float(withdrawal) < 0):
                        print("Value invalid, try again!")
                        withdrawal = input("Enter an amount to withdrawal (The withdrawal have positive): ")
                    elif (float(withdrawal) > 500):
                        print("You have exceeded the maximum withdrawal amount, try again!")
                        withdrawal = input("The withdrawal must be less than 500!\nEnter an amount to withdrawal: ")
                    elif (float(withdrawal) > balance):
                        print("The withdrawal must be small than the balance!")
                        withdrawal = input("Enter other amount to withdrawal:")
        
            balance -= float(withdrawal)
            qtdWithdrawal += 1
            #incrementar extrato ***********************************************
            print(f"\nWithdrawal sucessfull\nNew balance: {balance}\n--------------------------------------------------\n")
    
    elif (code == 's'): #incrementar extratos quando saque e depósito forem bem sucedidos
        print(f"""

""")

    else: #quando usuário digita letra não correspondente
        print("\nInvalid Operation, please select a correct letter!")
            

print("The central bank thanks you, see you next time!")