
#definición funciones
def calcula_divisores(numero:int):
    divisores = []
    for divisor in range(1, numero+1):
        if numero % divisor == 0:
            divisores.append(divisor)
    return divisores

comunes = []      
def max_com_div(lista1:list, lista2:list):
   
    elem_lista1 = len(lista1)
    elem_lista2 = len(lista2)
    
    for i in range(elem_lista1-1, -1, -1):
        if lista2.count(lista1[i]) == 1:
            return lista1[i]
    return -1

def simplifica_fracción(num1:int, num2:int, mcd:int):
    arriba = int(num1/mcd)
    abajo = int(num2/mcd)
    print(f"La división {num1}/{num2} simplificada es {arriba}/{abajo}")




print("Ingrese la fracción que desea operar")
num = int(input("Ingrese el numerador: "))
den = int(input("Ingrese el denominador: "))

lista_num = calcula_divisores(num)
lista_den = calcula_divisores(den)

mcd = max_com_div(lista_num, lista_den)
print(f"El M.C.D es: {mcd}")
simplif = simplifica_fracción(num, den, mcd)

