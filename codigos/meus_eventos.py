eventos = {}

qtdParticipantes = int(input("Quantidade de participantes: ").strip())

for _ in range (qtdParticipantes):
    linha = input("Participante, Tema").strip()

    nome, tema = linha.split(", ")

    if tema not in eventos:
        eventos[tema] = []

    eventos[tema].append(nome)

for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")