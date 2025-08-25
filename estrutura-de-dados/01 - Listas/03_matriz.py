matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

campo_minado = [
    [1,2,3,4],
    ["*", 0,"*", "*"],
    ["*", "*", 5, "*"],
    [4,6,0,7]]

print(campo_minado[3][3])