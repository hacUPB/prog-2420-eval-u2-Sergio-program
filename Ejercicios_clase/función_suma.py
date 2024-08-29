lista = [2,4,5,6,7,12,3,425,6,6,37,78,8,78]
acum = 0
cont = 0

num_ele = len(lista)

while cont < num_ele:
    acum += lista[cont]
    cont += 1

sumatoria = sum(lista)
print(f"Si el código es correcto, {acum} = {sumatoria}")

acum = 0
for elemento in lista:
    acum += elemento

print(f"Usando el bucle for la suma es: {acum}")