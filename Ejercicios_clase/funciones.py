#recibe numero de elementos, rango de valores y entrega uns lista.
#Recibe una lista de número flotante y devuelve el promedio.
#Calcula cuantos elementos de la lista están por encima del promedio.

from random import uniform

def crea_lista(cantidad:int, lim_inf:float, lim_sup:float): #parámetros de la función.
    #1. crear lista vacía.
    lista = []
    #2. utilizar un bucle
    for i in range(cantidad):
    #3. se genera núemro aleatorio.
        numero_aleat = uniform(lim_inf, lim_sup)
        #4. se agrega a la lista
        lista.append(numero_aleat)

    return lista

def calcula_promedio(datos:list):
    prom = sum(datos)/len(datos)
    return prom

def sobre_promedio(datos:list, promedio:float):
    cont = 0
    mayor = []
    for i in datos:
        if i > promedio:
            cont += 1
            mayor.append(i)
    return cont, mayor


#programa principal
aleatorios = crea_lista(100, -6.0, 10.0)
print(aleatorios)
promedio = calcula_promedio(aleatorios)
print(f"El promedio es {promedio}")
cont, mayor = sobre_promedio(aleatorios, promedio)
print(f"Hay {cont} datos mayor al promedio. Son: {mayor}")
