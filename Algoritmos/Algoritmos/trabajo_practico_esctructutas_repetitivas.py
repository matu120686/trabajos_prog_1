import random

# Ejercicio 1: Imprimir "Hola Mundo!"
"""
Mostrar los números del 0 al 100 (uno por línea):
"""
for i in range(101):
    print(i)

#Ejercicio 2
"""
Contar la cantidad de dígitos de un número ingresado:
"""
numero = input("Ingrese un número entero: ")
print("Cantidad de dígitos:", len(numero))

#Ejercicio 3
"""
Sumar todos los números entre dos valores (excluyendo ambos)
"""
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

inicio = min(a, b) + 1
fin = max(a, b)

suma = 0
for i in range(inicio, fin):
    suma += i

print("Suma:", suma)

#Ejercicio 4
"""
Sumar números hasta que el usuario ingrese 0
"""
suma = 0
while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        break
    suma += numero

print("Suma total:", suma)

#Ejercicio 5
"""
Juego: Adivinar número aleatorio entre 0 y 9
"""
numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break

#Ejercicio 6
"""
Números pares del 100 al 0 (decreciente)
"""
for i in range(100, -1, -2):
    print(i)


#Ejercicio 7
"""
 Sumar todos los números desde 0 hasta uno dado
"""
n = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(n + 1):
    suma += i

print("Suma:", suma)



#Ejercicio  8
"""
Ingresar 100 números y contar pares, impares, positivos y negativos
"""
pares = impares = positivos = negativos = 0

for _ in range(100):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num >= 0:
        positivos += 1
    else:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#Ejercicio 9
"""
Calcular la media de 100 números
"""
suma = 0

for _ in range(100):
    num = int(input("Ingrese un número: "))
    suma += num

media = suma / 100
print("Media:", media)

#Ejercicio 10
"""
 Invertir los dígitos de un número
"""
numero = input("Ingrese un número: ")
invertido = numero[::-1]
print("Número invertido:", invertido)




