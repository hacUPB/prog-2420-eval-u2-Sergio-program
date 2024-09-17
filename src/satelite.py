
alt_inicial = float(input("Ingrese la altitud inicial del satélite (en Km): "))
alt_minima = float(input("Ingrese la altitud mínima de orbita segura para el satélite (en Km): "))
cd = float(input("Ingrese el coeficiente de drag del satélite: "))
altitud = alt_inicial
cont = 0


delta_alt = cd * altitud

while altitud > alt_minima and delta_alt > 0.1:
    cd += 0.001
    cont += 1
    altitud -= delta_alt 
    delta_alt = cd * altitud
    print(f"En la orbita {cont} la altitud fue de {altitud} con una perdida de {delta_alt}")


if delta_alt < 0.1:
    print("El satélite logró estabilizarse en órbita")       
else:
    print(f"El satélite reingresó despues de {cont} órbitas, a una altura de {altitud}")

