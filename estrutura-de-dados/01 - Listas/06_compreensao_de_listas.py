# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)


numeros_2 = [4,26,32,8,18,1]

pares = [numero for numero in numeros_2 if numero %2 == 0]
print(pares)

cubo = [numero**3 for numero in numeros_2]
print(cubo)