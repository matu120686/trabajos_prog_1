# TP Intetgrador Matematica 1 - J

# Alumnos 

# Juan Compuetas Logicas
# Matias  Compuetas Logicas
# Nico Explicacion Decimal
# Andres Explicacion Decimal
# Noe Explicacion Decimal

# Conversor de Decimal a Binario

print("=== Conversor de Decimal a Binario ===")
print("Ingrese un número decimal: ")
decimal = int(input())
if decimal < 0:
    print("Por favor, ingrese un número positivo.")
elif decimal == 0:
    print("El número 0 en binario es: 0")
else:
    binario = []
    while decimal > 0:
        binario.append(decimal % 2)
        decimal = decimal // 2
    print("El número en binario es: ", end="")
    i = len(binario) - 1
    while i >= 0:
        print(binario[i], end="")
        i = i - 1
    print()
print("=== Fin del Programa ===")