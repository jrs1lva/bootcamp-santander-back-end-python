def cadastrar_usuario(contas):
    cpf = int(input("Digite seu CPF: ").strip()) #só permitir números

    if (cpf in contas):   
        print("CPF já cadastrado!")
    else:
        nome = input("Informe o nome completo: ")
        nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        cep = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        contas[cpf] = {"Nome": nome, "Nascimento": nascimento, "CEP": cep}
        print("Conta cadastrada com sucesso!")
    return contas

def listar_contas(contas):
    if (not contas):
        print("Ainda não existe conta.")
    else:
        print("\n📑 Contas cadastradas:")
        for cpf, dados in contas.items():
            print(f"CPF: {cpf} | Nome: {dados['Nome']} | Nascimento: {dados['Nascimento']} | CEP: {dados['CEP']}")

def depositar(saldo, valor, extrato, /): #Finalizado
    if (valor > 0):
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("\n▪▪▪ Depósito realizado com sucesso! ▪▪▪")
    else:
        print("[ERRO] Valor inserido menor que R$0.00")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor < 0:
        print("[ERRO] Valor inserido menor que R$0.00")
        
    elif numero_saques >= limite_saques:
        print("Limite de saque diário atingido!")

    elif valor > 500:
        print("[ERRO] Valor inserido maior que R$500.00")

    elif valor > saldo:
        if (valor <= saldo + limite):
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque com limite: R${valor:.2f}\n"
            print("Saque realizado com auxílio do limite")
        else:
            print("[ERRO] Valor inserido maior que saldo.")

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
[q] Sair

» """)
    return codigo 

def main():
    contas = {}
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
            if (not contas):
                print("Crie uma conta!")
            else:
                valor = float(input("Valor do depósito » R$"))
                saldo, extrato = depositar(saldo, valor, extrato)
        elif codigo == 's':
            if (not contas):
                print("Crie uma conta!")
            else:
                valor = float(input("Valor do saque » R$"))
                saldo, extrato, limite, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)
        elif codigo == 'e':
            if (not contas):
                print("Crie uma conta!")
            else:
                exibir_extrato(saldo, extrato = extrato)
        elif codigo == 'q':
                print("Volte sempre!")

        elif codigo == 'nc':
            cadastrar_usuario(contas)

        elif codigo == 'lc':
            if (not contas):
                print("Crie uma conta!")
            else:
                listar_contas(contas)
        else:
            print("Código inválido!")

main()