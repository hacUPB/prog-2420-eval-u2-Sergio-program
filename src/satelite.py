
alt_inicial = float(input("Ingrese la altitud inicial del satélite (en Km): "))
alt_minima = float(input("Ingrese la altitud mínima de orbita segura para el satélite (en Km): "))
cd = float(input("Ingrese el coeficiente de drag del satélite: "))
altitud = alt_inicial
cont = 0
delta_alt = 0


while altitud > alt_inicial or delta_alt < 100:
    delta_alt = cd * alt_inicial
    cd += 0.001
    cont += 1

if delta_alt < 100:
    print("El satélite logró estabilizarse en órbita")
altitud -= delta_alt
print(f"El satélite reingresó despues de {cont} órbitas, a una altura de {altitud}")

       


