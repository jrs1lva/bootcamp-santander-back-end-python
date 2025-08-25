matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])  # (1, "a", 2)
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

matriz_2 = (
    (1,4,5),
    (3,1,0),
    (3,1,5),
)

print((matriz_2[2][2]))