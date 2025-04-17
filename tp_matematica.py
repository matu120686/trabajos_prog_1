# ==============================================
# TP Integrador – Matemática - Grupo 1
# ==============================================

# Alumnos:
# ----------
# - Juan Martínez
# - Matias Olivera
# - Noe Bareiro
# - Nico Balverdi
# - Andres Muñoz

# Temas y Responsables:
# ----------------------
# Compuertas Lógicas:
# - Juan Martínez
# - Matias Olivera

# Explicación del Sistema Decimal:
# - Noe Bareiro
# - Nico Balverdi
# - Andres Muñoz

# ==============================================
# En este programa aplicamos la lógica binaria para convertir
# un número decimal a binario. Usamos estructuras condicionales
# (if/elif/else) que representan decisiones lógicas similares a 
# compuertas lógicas en electrónica digital (AND, OR, NOT).
# ==============================================

print("=== Conversor de Decimal a Binario ===")

# Solicitamos al usuario que ingrese un número decimal
print("Ingrese un número decimal: ")
decimal = int(input())

# Compuerta lógica: condición 'si el número es negativo'
# Simula una compuerta tipo NOT que rechaza el número
if decimal < 0:
    print("Por favor, ingrese un número positivo.")

# Compuerta lógica: condición 'si el número es igual a 0'
# Simula una compuerta de igualdad (==) que acepta solo el valor 0
elif decimal == 0:
    print("El número 0 en binario es: 0")

# Si no se cumple ninguna de las anteriores, ejecutamos la conversión
else:
    binario = []

    # Mientras el número sea mayor a 0, aplicamos divisiones sucesivas por 2
    # Aquí usamos módulo (%) y división entera (//), dos operaciones clave
    # para obtener los dígitos binarios
    while decimal > 0:
        binario.append(decimal % 2)  # Guardamos el resto de la división
        decimal = decimal // 2       # Reducimos el número dividiéndolo por 2

    # Mostramos el resultado en orden inverso (de mayor a menor bit)
    print("El número en binario es: ", end="")
    i = len(binario) - 1
    while i >= 0:
        print(binario[i], end="")
        i = i - 1

    print()

print("=== Fin del Programa ===")
