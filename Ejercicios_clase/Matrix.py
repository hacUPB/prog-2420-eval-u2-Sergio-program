from random import randint

#Función para crear matríz con datos aleatorios

def crea_matriz(filas:int, columnas:int, lim_inf:int, lim_sup:int):


    lista = []
    for i in range(filas):
        lista.append([])
        for j in range(columnas):
            n = randint(lim_inf, lim_sup)
            lista[i].append(n)
    return lista

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de colunmas: "))
lim_inf = int(input("Ingrese el número menor: "))
lim_sup = int(input("Ingrese el número mayor: "))


matriz = crea_matriz(filas, columnas, lim_inf, lim_sup)
print(matriz)
#for i in range(filas):
    #print("|", end=' ')
    #for j in range(columnas):
        #print(f"{lista[i][j]:^5}|", end= ' ')
    #print()