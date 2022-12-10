#Ejercicio 2: Análisis + Desarrollo
# La serie de Fibonacci se construye utilizando la siguiente relación de recurrencia: Fn = Fn1 + Fn2, donde F1 = 1 y F2 = 1. Por ende, los primeros doce términos de esta serie son: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# Ahora, consideremos los divisores de estos términos:
# 1 = 1
# 1 = 1
# 2 = 1, 2
# 3 = 1, 3
# 5  = 1, 5
# 8 = 1, 2, 4, 8
# 13 = 1, 13
# 21 = 1, 3, 7, 21
# 34 = 1, 2, 17, 34
# 55 = 1, 5, 11, 55
# 89 = 1, 89
# 144 = 1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 36, 48, 72, 144

from math import sqrt
def get_ListaFibonacci(n):
    lista = [0, 1]
    for i in range(3, n):
        lista.append(lista[len(lista) - 1] + lista[len(lista) - 2])
    return lista

def get_Divisores(n):
    divs = {1,n}
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            divs.update((i,n//i))
    return divs

def encontrar_divisor_mayor_mil(fibonaccis):
    constante = 12
    contador = 0
    data = {"fibonacci": 0,"divisores": {}}
    for i in range(0, int(len(fibonaccis)/constante)):
        contador = contador + constante
        fib = fibonaccis[contador]
        divisores = get_Divisores(fib)
        if len(list(divisores)) >= 1000:
            data["fibonacci"] = fib
            data["divisores"] = divisores
            return data
    return data

fibonaccis = get_ListaFibonacci(100)
data = encontrar_divisor_mayor_mil(fibonaccis)
print('Fibonacci: ',data["fibonacci"])
print('Cantidad de divisores: ',len(list(data["divisores"])))
print('Divisores: ',data["divisores"])
