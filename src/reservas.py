
import random
from os import system

distancia = 0
ciudades = ["Medellín", "Cartagena", "Bogotá"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
asientos = ["Ventana", "Intermedio", "Pasillo", "Aleatorio"]

fila = random.randint(1, 29)
vuelo = random.randint(1111, 9999)


adj = input("¿Es usted Sr. ó Sra. ?:")
nombre = input("Ingrese su nombre completo:")
print(f"{adj} {nombre} Bienvenido a FastFast Airlines")

while True:
        origen = input("Ingrese su ciudad de origen (Medellín, Bogotá, Cartagena):")
        if origen not in ciudades:
            print("Ingrese una opción válida")
        else:
            break
while True:
        destino = input("Ingrese su ciudad de destino (Medellín, Bogotá, Cartagena):")
        if destino not in ciudades:
            print("Ingrese una opción válida")
        else:
            break

fecha =input("Ingrese la fecha del viaje (dd.mm.yy):")

while True:
    dia = input("Ingrese el día de la semana que viaja: (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado ó Domingo):")
    if dia not in dias:
        print("El día no es válido")
    else:
        break     

if destino == "Medellín":
    if origen == "Bogotá":
            distancia == 1
    elif distancia == 2:

        if destino == "cartagena":
                distancia == 2

        if destino == "Bogotá":
                    if origen == "Medellín":
                            distancia == 1
                    elif distancia == 2:
                           pass
if dia == "Lunes":
    if distancia == 1:
            precio = 79.900
if dia == "Martes":
    if distancia == 1:
            precio = 79.900
if dia == "Miércoles":
    if distancia == 1:
            precio = 79.900
if dia == "Jueves":
    if distancia == 1:
            precio = 79.900
if dia == "Viernes":
    if distancia == 1:
            precio = 79.900
if dia == "Sábado":
        precio = 156.000
if dia == "Domingo":
     precio = 156.000

else:
    
    if dia == "Lunes":
        if distancia == 2:
            precio = 119.900

    if dia == "Martes":
        if distancia == 2:
            precio = 119.900
    
    if dia == "Miércoles":
        if distancia == 2:
            precio = 119.900
    
    if dia == "Jueves":
        if distancia == 2:
            precio = 119.900

    if dia == "viernes":
        if distancia == 2:
            precio = 119.900
    
    if dia == "Sábado":
        precio = 213.000
    if dia == "Domingo":
         precio = 213.000

asiento = input("El proceso está casi terminado, seleccione su asiento de preferencia (Ventana, Intemedio, Pasillo, Aleatorio):")

if asiento == "Ventana":
    asiento = "A"
if asiento == "Intermedio":
    asiento = "E"
if asiento == "Pasillo":
    asiento = "C"
if asiento == "Aleatorio":
     asiento = "F"



print(f"Su reserva ha sido confirmada.\nEl vuelo desde {origen} hacia {destino} ha sido confirmado con éxito, para el día {dia} {fecha}\n Vuelo: {vuelo} Pasajero: {nombre} Asiento: {fila}{asiento} por un precio total de ${precio}.")
system ("cls")