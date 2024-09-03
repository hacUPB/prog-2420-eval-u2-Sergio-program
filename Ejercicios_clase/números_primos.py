from os import system

while True: 
    print("1. Calcular primo\n2. Calcular par\n3. Salir")
    opcion = int(input("Ingrese la opción:"))

    if opcion == 1:
        system ("cls")
        numero = int(input("Ingrese el número a probar:"))
        cont = 0
        control = 1

        while control <= numero:
            if numero % control == 0:
                cont += 1
            control += 1
       
        if cont > 2: 
            print(f"{numero} no es primo")
        else:
            print(f"{numero} es primo")
    elif opcion == 2:
        system ("cls")
        numero = int(input("Ingrese el número a probar:"))
        if numero % 2 == 0:
            print(f"{numero} es par")
        else:
            print(f"{numero} es impar")
    
    elif opcion == 3:
        break
    else: 
        print("Opción no valida")
