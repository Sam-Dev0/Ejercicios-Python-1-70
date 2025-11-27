
"""I. Ejercicios Básicos"""
# Básico: Suma de dos números
try:
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    suma = num1 + num2
    print(f"La suma de {num1} y {num2} es: {suma}")
except ValueError:
    print("Error: Por favor, ingresa solo números enteros.")

# Intermedio: Conversión de Temperatura
try:
    celsius = float(input("Ingresa la temperatura en Celsius: "))
    # F = C * 9/5 + 32
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
except ValueError:
    print("Error: Por favor, ingresa un valor numérico válido.")


import math

# Avanzado: Cálculo de Hipotenusa
try:
    cateto_a = float(input("Ingresa la longitud del cateto a: "))
    cateto_b = float(input("Ingresa la longitud del cateto b: "))
    
    # Teorema de Pitágoras: c = sqrt(a^2 + b^2)
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    
    print(f"La longitud de la hipotenusa es: {hipotenusa:.3f}")
except ValueError:
    print("Error: Por favor, ingresa valores numéricos positivos.")
except Exception as e:
    print(f"Ocurrió un error: {e}")


"""II. Toma de Decisiones (if-elif-else)"""
# Básico: Clasificación de número
try:
    num = float(input("Ingresa un número: "))
    
    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
except ValueError:
    print("Error: Ingresa un número válido.")


# Intermedio: Verificación de Edad
try:
    edad = int(input("Ingresa tu edad: "))
    
    if edad >= 18:
        print("Eres mayor de edad y puedes votar.")
    elif edad >= 0 and edad < 18:
        print(f"Eres menor de edad. Te faltan {18 - edad} años para poder votar.")
    else:
        print("Edad no válida (debe ser un valor positivo).")
except ValueError:
    print("Error: Ingresa un número entero para la edad.")


# Avanzado: Cálculo de Impuestos
try:
    salario = float(input("Ingresa tu salario anual: "))
    tasa_impuesto = 0.0
    
    if salario <= 0:
        print("Salario no válido.")
    elif salario < 10000:
        tasa_impuesto = 0.0
    elif salario <= 50000:
        tasa_impuesto = 0.10  # 10%
    else:
        tasa_impuesto = 0.20  # 20%
        
    impuesto = salario * tasa_impuesto
    print(f"Tu salario es ${salario:,.2f}.")
    print(f"La tasa de impuesto aplicada es: {tasa_impuesto * 100}%.")
    print(f"El monto de impuesto a pagar es: ${impuesto:,.2f}")
    print(f"Salario neto (aproximado): ${salario - impuesto:,.2f}")

except ValueError:
    print("Error: Ingresa un valor numérico válido para el salario.")


"""III. Selección de Casos"""
# Básico: Días de la Semana
try:
    dia_num = int(input("Ingresa un número (1-7) para el día de la semana: "))
    
    if dia_num == 1:
        print("Lunes")
    elif dia_num == 2:
        print("Martes")
    elif dia_num == 3:
        print("Miércoles")
    elif dia_num == 4:
        print("Jueves")
    elif dia_num == 5:
        print("Viernes")
    elif dia_num == 6:
        print("Sábado")
    elif dia_num == 7:
        print("Domingo")
    else:
        print("Número fuera del rango (1-7).")
except ValueError:
    print("Error: Ingresa un número entero.")


# Intermedio: Calificación Literal
try:
    nota = int(input("Ingresa la calificación numérica (0-100): "))
    
    if 90 <= nota <= 100:
        print("Calificación: A (Excelente)")
    elif 80 <= nota < 90:
        print("Calificación: B (Notable)")
    elif 70 <= nota < 80:
        print("Calificación: C (Aprobado)")
    elif 60 <= nota < 70:
        print("Calificación: D (Suficiente)")
    elif 0 <= nota < 60:
        print("Calificación: F (Reprobado)")
    else:
        print("Calificación fuera de rango.")
except ValueError:
    print("Error: Ingresa un número entero.")


# Avanzado: Calculadora Simple
try:
    num1 = float(input("Ingresa el primer número: "))
    operador = input("Ingresa el operador (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo número: "))
    resultado = 0
    
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: División por cero.")
            resultado = "Indefinido"
    else:
        print("Error: Operador no válido.")
        resultado = "Inválido"

    if resultado != "Indefinido" and resultado != "Inválido":
        print(f"El resultado de {num1} {operador} {num2} es: {resultado:.2f}")

except ValueError:
    print("Error: Asegúrate de ingresar números válidos.")


"""IV. Ciclo Repetitivo “for”"""
# Básico: Contar hasta 10 con for
for i in range(1, 11): # range(inicio, fin + 1)
    print(i)


# Intermedio: Suma de los primeros N números
try:
    N = int(input("Ingresa un número entero N: "))
    suma_total = 0
    
    for i in range(1, N + 1):
        suma_total += i
        
    print(f"La suma de los números del 1 al {N} es: {suma_total}")
except ValueError:
    print("Error: Ingresa un número entero válido.")


# Avanzado: Factorial de un número
try:
    N = int(input("Ingresa un número entero no negativo para calcular su factorial: "))
    
    if N < 0:
        print("El factorial solo está definido para números no negativos.")
    elif N == 0:
        factorial = 1
        print("El factorial de 0 es: 1")
    else:
        factorial = 1
        for i in range(1, N + 1):
            factorial *= i
        print(f"El factorial de {N} ({N}!) es: {factorial}")
except ValueError:
    print("Error: Ingresa un número entero.")


"""V. Ciclo Repetitivo “while”"""
# Básico: Contador descendente (while)
while contador >= 1:
    print(contador)
    contador -= 1

# Intermedio: Validar una contraseña (while)
contrasena_correcta = "secreto123"
intento = ""
intentos = 0

while intento != contrasena_correcta:
    intento = input("Ingresa la contraseña: ")
    intentos += 1
    if intento == contrasena_correcta:
        print(f"¡Contraseña correcta! Acceso concedido después de {intentos} intentos.")
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")


# Avanzado: Encontrar el primer número divisible
try:
    X = int(input("Ingresa un número entero X (excepto 0): "))
    
    if X == 0:
        print("X no puede ser 0.")
    else:
        numero_actual = 1
        encontrado = False
        
        while not encontrado:
            # Condición: divisible por X y por 13
            if numero_actual % X == 0 and numero_actual % 13 == 0:
                print(f"El primer número divisible por {X} y por 13 es: {numero_actual}")
                encontrado = True # Detiene el ciclo
            else:
                numero_actual += 1
                
except ValueError:
    print("Error: Ingresa un número entero.")


"""VI. Ciclo Repetitivo “do-while”"""
# Básico: Saludo al menos una vez (do-while simulado)
while True:
    nombre = input("Ingresa tu nombre: ")
    print(f"¡Hola, {nombre}!")
    
    continuar = input("¿Deseas saludar a otra persona? (s/n): ").lower()
    if continuar != 's':
        break # Sale del ciclo si la respuesta no es 's'

# Intermedio: Menú de Opciones (do-while simulado)
opcion = -1

while True:
    print("\n--- MENÚ ---")
    print("1. Ver perfil")
    print("2. Configuración")
    print("3. Ayuda")
    print("0. Salir")
    
    try:
        opcion = int(input("Elige una opción (0-3): "))
        
        if opcion == 1:
            print("Accediste a 'Ver perfil'.")
        elif opcion == 2:
            print("Accediste a 'Configuración'.")
        elif opcion == 3:
            print("Accediste a 'Ayuda'.")
        elif opcion == 0:
            print("Saliendo del programa. ¡Adiós!")
            break # Sale del ciclo
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            
    except ValueError:
        print("Error: Ingresa un número entero.")



import random

# Avanzado: Adivinar Número con Pista (do-while simulado)
numero_secreto = random.randint(1, 100)
intento = 0

print("Adivina el número secreto entre 1 y 100.")
while True:
    try:
        intento = int(input("Ingresa tu intento: "))
        
        if intento < numero_secreto:
            print("Pista: ¡El número es MAYOR!")
        elif intento > numero_secreto:
            print("Pista: ¡El número es MENOR!")
        else:
            print(f"¡Felicitaciones! Adivinaste el número secreto: {numero_secreto}.")
            break # Sale del ciclo
            
    except ValueError:
        print("Error: Por favor, ingresa un número entero.")

"""VII. Vectores (Listas en Python)"""
# Básico: Imprimir elementos de un vector
nombres = ["Ana", "Beto", "Carlos", "Diana", "Ernesto"]
print("Lista de nombres:")
for nombre in nombres:
    print(f"- {nombre}")


# Intermedio: Suma y promedio de un vector
numeros = []
for i in range(5):
    try:
        num = float(input(f"Ingresa el número #{i+1}: "))
        numeros.append(num)
    except ValueError:
        print("Error. Se usará 0 como valor predeterminado.")
        numeros.append(0.0)

if numeros:
    suma = sum(numeros)
    promedio = suma / len(numeros)
    print(f"Los números ingresados son: {numeros}")
    print(f"La suma total es: {suma:.2f}")
    print(f"El promedio es: {promedio:.2f}")
else:
    print("No se ingresaron números válidos.")


# Avanzado: Encontrar el mayor y su posición
numeros_avanzado = []
num_elementos = 6

for i in range(num_elementos):
    try:
        num = float(input(f"Ingresa el número #{i+1}: "))
        numeros_avanzado.append(num)
    except ValueError:
        print("Error. Se omitirá este valor.")

if numeros_avanzado:
    max_valor = numeros_avanzado[0]
    for num in numeros_avanzado:
        if num > max_valor:
            max_valor = num
            

    posicion = numeros_avanzado.index(max_valor)
    
    print(f"El vector es: {numeros_avanzado}")
    print(f"El número más grande es: {max_valor}")
    print(f"Se encuentra en la posición (índice) {posicion}")
else:
    print("El vector está vacío o solo contiene valores no válidos.")

"""VIII. Matrices"""
# Básico: Imprimir una Matriz 3x2
matriz_basica = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print("Contenido de la Matriz:")
for fila in matriz_basica:
    for elemento in fila:
        print(f"{elemento}\t", end="")
    print() 


# Intermedio: Suma de elementos de una Fila
matriz_intermedia = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

try:
    num_fila = int(input("Ingresa el número de fila a sumar (0, 1 o 2): "))
    
    if 0 <= num_fila < len(matriz_intermedia):
        fila_seleccionada = matriz_intermedia[num_fila]
        suma_fila = sum(fila_seleccionada)
        print(f"La fila seleccionada ({num_fila}) es: {fila_seleccionada}")
        print(f"La suma de los elementos de la fila {num_fila} es: {suma_fila}")
    else:
        print("Número de fila fuera de rango.")
except ValueError:
    print("Error: Ingresa un número entero.")



# Avanzado: Suma de dos Matrices 2x2

def leer_matriz(nombre):
    """Pide al usuario los elementos de una matriz 2x2."""
    matriz = []
    print(f"\n--- Ingresa los elementos de la Matriz {nombre} (2x2) ---")
    for i in range(2):
        fila = []
        for j in range(2):
            try:
                val = int(input(f"Ingresa el valor para {nombre}[{i}][{j}]: "))
                fila.append(val)
            except ValueError:
                print("Valor no válido, usando 0.")
                fila.append(0)
        matriz.append(fila)
    return matriz

matriz_A = leer_matriz("A")
matriz_B = leer_matriz("B")
matriz_C = [[0, 0], [0, 0]] 


for i in range(2): 
    for j in range(2): 
        matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]

print("\n--- Resultado de la Suma (Matriz A + Matriz B) ---")
for fila in matriz_C:
    print(fila)


