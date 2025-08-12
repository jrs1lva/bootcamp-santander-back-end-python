def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")

    print("Obrigado por ser nosso cliente")



def depositar(valor):
    saldo = 500
    if valor > 0:
        saldo += valor
        print("Saldo da conta:", saldo)




sacar(600)
depositar(2)