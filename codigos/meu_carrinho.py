carrinho = []
total = 0.0

n = int(input("Digite a quantidade de itens: ").strip())

for _ in range(n):
    linha = input("""Informe o item seguido de uma vírgula e o valor, exemplo:
    Leite, 5.00
    => """).strip()
    
    item, preco = linha.split(", ")
    carrinho.append((item, preco))
    total += float(preco)

for item, preco in carrinho:
    print(f"{item}: R${preco}")

print(f"Total: R${total}")