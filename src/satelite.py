
alt_inicial = float(input("Ingrese la altitud inicial del satélite: "))
alt_minima = float(input("Ingrese la altitud mínima de orbita segura para el satélite: "))
cd = float(input("Ingrese el coeficiente de drag del satélite: "))
altitud = alt_inicial
cont = 0
    
while altitud > alt_minima:
    altitud *= cd
    cd += 0.00000000001
    cont += 1
if altitud == alt_minima:
        print(f"El satélite se estabilizó después de {cont} orbitas")
else:
        print(f"El satélite no logró estabilizarse después de {cont} orbitas, y reingresó a la atmosfera con una altitud de {altitud}")



