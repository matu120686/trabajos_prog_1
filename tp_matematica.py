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

# Explicación del método de conversión de un número decimal a binario:
# - Noe Bareiro
# - Nico Balverdi
# - Andres Muñoz

# ==============================================
# En este programa utilizamos lógica booleana para convertir
# un número decimal a binario. A través de estructuras condicionales
# (if/elif/else), evaluamos condiciones verdaderas o falsas.
# Aunque no implementamos compuertas lógicas directamente,
# la lógica que usamos se basa en los mismos principios
# que las compuertas AND, OR y NOT de la electrónica digital.
# ==============================================

print("=== Conversor de Decimal a Binario ===")

# Solicitamos al usuario que ingrese un número decimal
print("Ingrese un número decimal: ")
decimal = int(input())

# Evaluamos si el número es negativo
# Esta condición representa una lógica tipo NOT: "no es un número válido"
if decimal < 0:
    print("Por favor, ingrese un número positivo.")

# Evaluamos si el número es igual a 0
# Esta comparación se basa en la lógica de igualdad (==)
elif decimal == 0:
    print("El número 0 en binario es: 0")

# Si no se cumple ninguna de las anteriores (el número es positivo y distinto de 0)
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
