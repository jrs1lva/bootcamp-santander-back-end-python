linguagens = ["python", "js", "c", "java", "csharp", "x", "c", "c"]

#esse metodo conta o primeiro elemento encontrado
print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

#solução
for indice, i in enumerate(linguagens):
    if i == "c":
        print(indice)