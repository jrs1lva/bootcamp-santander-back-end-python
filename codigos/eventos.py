# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# Loop para armazenar participantes e seus temas
for _ in range(n):
    linha = input().strip()
    
    # Separar nome e tema (antes e depois da vírgula)
    nome, tema = linha.split(", ")
    
    # Se o tema ainda não existir no dicionário, cria uma lista vazia
    if tema not in eventos:
        eventos[tema] = []
    
    # Adiciona o participante na lista do tema
    eventos[tema].append(nome)

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")