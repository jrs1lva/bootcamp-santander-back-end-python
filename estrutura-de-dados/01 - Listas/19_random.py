import random
sorteio = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(random.choice(sorteio))  # retorna um valor aleatório da lista
print(random.sample(sorteio, 5))
print(random.choices(sorteio, k=3))  # retorna 3 valores aleatórios da lista, podendo repetir
random.shuffle(sorteio)  # embaralha a lista
print(sorteio)