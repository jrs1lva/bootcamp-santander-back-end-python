carrinho = []
total = 0.0

qtdItens = int(input("Informe a quantidade de itens: ").strip())

for _ in range(qtdItens):
    linha = input("Digite o item e o valor, exemplo: Leite 5.00\n=> ").strip()
    posicao_espaco = linha.rfind(" ")

    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:].strip())

    carrinho.append((item, preco))
    total += preco

print("")

for item, valor in carrinho:
    print(f"{item}: R${preco}")

print(f"\nTotal: R${total}")