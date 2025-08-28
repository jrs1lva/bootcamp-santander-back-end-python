def criar_usuario(nome, nascimento, cpf, **endereco):
    print()

def extrato(saldo, /, *, extrato):
    '''print(f"""{saldo}
Quantity of deposit: {qtdDeposit}
Quantity of withdrawal: {qtdWithdrawal}
Actualy balance: ${balance:.2f}
""")'''

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if (numero_saques <= limite_saques):
        if valor > saldo:
            print("[ERRO] valor solicitado maior que o saldo da conta")
        else:
            saldo -= valor
            numero_saques += 1
            return saldo, extrato
    else:
        print("[ERRO] limite de saque diário alcançado.")

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        return saldo, extrato
    else:
        print("[ERRO] Valor depositado menor que 0")