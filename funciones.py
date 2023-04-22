"""def ordenarDesc(numero1,numero2):
    if numero1>numero2:
        return numero1,numero2
    elif numero1==numero2:
        
        return f"{numero1} es igual a {numero2}"
    else:    
        return numero2,numero1
print (ordenarDesc(205,200))            


#recursividad: uso llamado de la misma funcion declarada

#imprimir dos nueros del 10 al 1

def mostrar(num):
    print(num)
    if num >0:
        mostrar(num-1)
mostrar(10)"""


#factorial de un numero


def factorial (valor):
    if valor>1:
        valor=valor * factorial(valor - 1)
    return valor
print(factorial(6))   




