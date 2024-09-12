import random 
from os import system
from datetime import datetime


distancia = 0
ciudades = ["MDE", "CTG", "BOG"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
asientos = ["V", "I", "P", "A"]
adjetivos = ["Sr", "Sra"]

fila = random.randint(1, 29)
vuelo = random.randint(1111, 9999)

while True:
    adj = input("¿Es usted Sr. ó Sra. ?: ").capitalize()
    if adj not in adjetivos:
        print("Revise la opción ingresada")
    else:
        break 

nombre = input("Ingrese su nombre: ").capitalize()
apellido = input("Ingrese su apellido: ").capitalize()
print(f"{adj} {nombre} {apellido} Bienvenido a FastFast Airlines")

while True:
    origen = input("Ingrese su ciudad de origen (Medellín: MDE, Bogotá: BOG, Cartagena: CTG): ").upper()
    if origen not in ciudades:
        print("Ingrese una opción válida")
    else:
        break

while True:
    destino = input("Ingrese su ciudad de destino (Medellín: MDE, Bogotá: BOG, Cartagena: CTG): ").upper()
    if destino not in ciudades:
        print("Ingrese una opción válida")
    else:
        break

while True:
    fecha_ingresada = input("Ingresa una fecha en formato dd/mm/yyyy: ")
    try:
        fecha_usuario = datetime.strptime(fecha_ingresada, "%d/%m/%Y")
        fecha_actual = datetime.now()
        if fecha_usuario < fecha_actual:
            print("La fecha ingresada es incorrecta, por favor revisela.")
        else: 
            break
    except ValueError:
        print("El formato de la fecha es incorrecto. Por favor, ingresa una fecha válida en el formato dd/mm/yyyy.")
dia = fecha_actual.weekday()

dia =dias [dia] 

#while True:
    #dia = input("Ingrese el día de la semana que viaja (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado, Domingo): ")
    #if dia not in dias:
        #print("El día no es válido")
    #else:
        #break     

# Determinar la distancia entre origen y destino
if origen == "BOG" and destino == "MDE":
    distancia = 1
elif origen == "MDE" and destino == "BOG":
    distancia = 1
elif (origen == "BOG" and destino == "CTG") or (origen == "CTG" and destino == "BOG"):
    distancia = 2
elif (origen == "MDE" and destino == "CTG") or (origen == "CTG" and destino == "MDE"):
    distancia = 2

# Determinar el precio del vuelo basado en la distancia y el día de la semana
if distancia == 1:
    if dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
        precio_final = 79900
    elif dia in ["Sábado", "Domingo"]:
        precio_final = 156000
elif distancia == 2:
    if dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
        precio_final = 119900
    elif dia in ["Sábado", "Domingo"]:
        precio_final = 213000

# Selección de asiento
while True:
    asiento = input("El proceso está casi terminado, seleccione su asiento de preferencia (Ventana: V, Intermedio: I, Pasillo: P, Aleatorio: A): ").upper()
    if asiento not in asientos:
        print("Ingrese una opción válida")
    else:
        break

if asiento == "V":
    asiento = "A"
elif asiento == "I":
    asiento = "E"
elif asiento == "P":
    asiento = "C"
elif asiento == "A":
    asiento = "F"

system("cls" if system == "nt" else "clear")
print(f"Su reserva ha sido confirmada.\nEl vuelo desde {origen} hacia {destino} ha sido confirmado con éxito, para el día {dia} {fecha_ingresada}\nVuelo: {vuelo} Pasajero: {nombre} {apellido} Asiento: {fila}{asiento} por un precio total de ${precio_final}")