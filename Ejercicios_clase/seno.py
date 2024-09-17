from math import factorial, sin, pi
num_terminos = 1000
x = 45
resultado = 0
for i in range(num_terminos):
    signo = (-1)**i
    exponente = (2*i + 1)
    termino = signo * x** exponente / factorial(exponente)
    resultado += termino

    seno_math = sin(x)
print(f"sen{x} = {resultado}-----debe dar {seno_math}")
