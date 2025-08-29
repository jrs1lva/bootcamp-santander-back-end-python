def depositar(saldo, valor, extrato): #Finalizado
    if (valor > 0):
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("\n▪▪▪ Depósito realizado com sucesso! ▪▪▪")
    else:
        print("Valor inválido!")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques > limite_saques:
        print("Limite de saque diário atingido!")

    elif valor > 500:
        print("Saque maior que 500")

    elif "Depósito" not in extrato:
        print("Ainda não foram realizadas as movimentações!")



    elif valor > saldo:
        if (valor <= saldo + limite):
            """
            saldo = 200
            limite = 100
            saque = 250
            saldo - saque = -50
            -50(saldo) -100(limite) = 50
            """
            saldo -= valor
            numero_saques += 1
            limite = limite + saldo
            extrato += f"Saque com limite: R${valor:.2f}\n"
            print("Saque realizado com auxílio do limite")

        else:
            print("Valor de saque indisponível")

    else:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque: R${valor:.2f}\n"
        print("▪▪▪ Saque realizado com sucesso! ▪▪▪")

    return saldo, extrato, limite, numero_saques
    
def exibir_extrato(saldo, /, *, extrato): #Finalizado
    print("\n📄 ▪▪▪ EXTRATO ▪▪▪ 📄\n")
    if extrato == '':
        print("Ainda não houveram movimentações nessa conta.")
    else:
        print(extrato)
    print(f"\nSaldo atual: R${saldo:.2f}")

def menu(saldo): #Finalizado
    codigo = input(f"""▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪ MENU ▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪
                
Seu saldo: ${saldo}

Digite uma letra para escolher a operação:
[d] Depósito
[s] Saque
[e] Extrato
[nc] Nova Conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair

» """)
    return codigo 

def main():
    saldo = 0.0
    codigo = ''
    extrato = ''
    limite = 500
    numero_saques = 0
    LIMITE_SAQUES = 3

    nome = input("Oi! Qual seu nome? » ").strip()
    print(f"Oi {nome.title()}, Bem vindo ao Banco Central:")
    while (codigo != 'q'):
        codigo = menu(saldo)

        if codigo == 'd':
            valor = float(input("Valor do depósito » "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif codigo == 's':
            valor = float(input("Valor do saque » "))
            saldo, extrato, limite, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)
        elif codigo == 'e':
            exibir_extrato(saldo, extrato = extrato)
        elif codigo == 'q':
            print("Volte sempre!")

        elif codigo == 'nc':
            print()
        elif codigo == 'lc':
            print()
        elif codigo == 'nu':
            print()
        else:
            print("Código inválido!")


main()