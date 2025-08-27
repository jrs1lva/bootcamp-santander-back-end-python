def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

def func_3():
    print("Olá mundo!")

print(calcular_total([3,4,5,6]))
print(retorna_antecessor_sucessor(5))
print(func_3())