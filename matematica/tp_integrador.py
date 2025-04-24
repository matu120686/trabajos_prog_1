# ==============================================
# TP Integrador – Matemática - Grupo 1
# ==============================================

# Alumnos:
# ----------
# - Juan Martínez
# - Juan Barbero
# - Matias Olivera
# - Nico Balverdi
# - Andres Muñoz

# Temas y Responsables:
# ----------------------
# Compuertas Lógicas:
# - Juan Martínez
# - Matias Olivera

# Explicación del método de conversión de un número decimal a binario:
# - Nico Balverdi
# - Juan Barbero
# - Andres Muñoz

# ==============================================
# En este programa utilizamos lógica booleana para convertir
# un número decimal a binario. A través de estructuras condicionales
# (if/else), evaluamos condiciones verdaderas o falsas.
# Aunque no implementamos compuertas lógicas directamente,
# la lógica que usamos se basa en los mismos principios
# que las compuertas AND, OR y NOT de la electrónica digital.
# ==============================================

print("=== Conversor de Decimal a Binario ===")
# Se define una bandera que controlará si todo el proceso se repite con un nuevo
# número decimal ingresado por el usuario.
bandera = 1
# Solicitamos al usuario que ingrese un número decimal
decimal = int(input("Ingrese un número decimal: "))

# Evaluamos si el número es negativo
# Se evalua si el número es menor que 0 y de ser así,
# se le pide al usuario que ingrese un número positivo
while bandera == 1:
    while decimal < 0:
        decimal = int(input("Por favor, ingrese un número positivo."))
    # Evaluamos si el número es igual a 0
    # Esta comparación se basa en la lógica de igualdad (==)
    if decimal == 0:
        print("El número 0 en binario es: 0")
        bandera = 0
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
        # Preguntamos al usuario si desea continuar con otro número
        print("¿Desea ingresar otro número? (1: Sí, 0: No): ")
        bandera = int(input())
        # En caso de que el usuario decida continuar convirtiendo números
        # cargamos el nuevo número en la variable decimal para repetir el proceso
        if bandera == 1:
            decimal = int(input("Ingrese un número decimal: "))

print("=== Fin del Programa ===")