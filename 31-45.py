# 31. Programa que permita determinar cuantos estudiantes son mayores de edad 
# en un grupo de 20 estudiantes. 
TOTAL_ESTUDIANTES = 20
mayores_edad = 0
i = 1

for i in range(1, TOTAL_ESTUDIANTES + 1):
    while True:
        try:
            edad = int(input(f"Ingrese la edad del estudiante {i}/{TOTAL_ESTUDIANTES}: "))
            if edad < 0:
                print("La edad no puede ser negativa. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    # Condición para verificar si es mayor de edad (>= 18)
    if edad >= 18:
        mayores_edad += 1

print(f"\nResumen:")
print(f"Total de estudiantes: {TOTAL_ESTUDIANTES}")
print(f"Estudiantes mayores de edad (>= 18 años): {mayores_edad}")
print(f"Estudiantes menores de edad: {TOTAL_ESTUDIANTES - mayores_edad}")



# 32. Programa que permita determinar cuantos hombres y mujeres hay 
# en un curso de 25 estudiantes.
TOTAL_ESTUDIANTES = 25
conteo_hombres = 0
conteo_mujeres = 0


for i in range(1, TOTAL_ESTUDIANTES + 1):

    while True:
        genero = input(f"Ingrese el género del estudiante {i}/{TOTAL_ESTUDIANTES} (H para Hombre, M para Mujer): ").strip().upper()
        if genero == 'H':
            conteo_hombres += 1
            break
        elif genero == 'M':
            conteo_mujeres += 1
            break
        else:
            print("Género inválido. Ingrese 'H' o 'M'.")

print(f"\nResumen:")
print(f"Total de estudiantes: {TOTAL_ESTUDIANTES}")
print(f"Cantidad de hombres: {conteo_hombres}")
print(f"Cantidad de mujeres: {conteo_mujeres}")



# 33. Programa para calcular la edad promedio de un grupo de 15 estudiantes.
TOTAL_ESTUDIANTES = 15
suma_edades = 0


for i in range(1, TOTAL_ESTUDIANTES + 1):
    while True:
        try:
            edad = int(input(f"Ingrese la edad del estudiante {i}/{TOTAL_ESTUDIANTES}: "))
            if edad < 0 or edad > 120:
                print("Edad fuera de rango normal. Intente de nuevo.")
                continue
            suma_edades += edad
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

if TOTAL_ESTUDIANTES > 0:
    promedio_edad = suma_edades / TOTAL_ESTUDIANTES
    print(f"\nResumen:")
    print(f"Suma total de edades: {suma_edades}")
    print(f"La edad promedio del grupo es: {promedio_edad:.2f} años.")
else:
    print("No hay estudiantes para calcular el promedio.")
    
    

# 34. Programa que permita calcular la estatura promedio de un grupo de 18 
# estudiantes y luego tomar decisiones. 
TOTAL_ESTUDIANTES = 18
suma_estaturas = 0

for i in range(1, TOTAL_ESTUDIANTES + 1):
    while True:
        try:
            estatura = float(input(f"Ingrese la estatura en cm del estudiante {i}/{TOTAL_ESTUDIANTES}: "))
            if estatura <= 0:
                print("La estatura debe ser positiva. Intente de nuevo.")
                continue
            suma_estaturas += estatura
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número (ej. 175.5).")

if TOTAL_ESTUDIANTES > 0:
    promedio_estatura = suma_estaturas / TOTAL_ESTUDIANTES
    print(f"\nLa estatura promedio del grupo es: {promedio_estatura:.2f} cm.")

    print("Clasificación:")
    if promedio_estatura < 140:
        print("Estudiantes muy bajos.")
    elif promedio_estatura <= 170:
        print("Estudiantes de estatura normal.")
    else:
        print("Estudiantes muy altos.")
else:
    print("No hay estudiantes para calcular el promedio.")
    
# 35. Programa que muestre en pantalla los múltiplos de 3 teniendo como límite 
# el número 99. 
print("Los múltiplos de 3 son:")

for i in range(3, 100, 3):
    print(i, end=" ")
print("\n(Fin de la lista)")



# 36. Programa que imprima la tabla de multiplicar hasta 10 de un número 
# cualquiera ingresado por el usuario. 
numero = 0

while True:
    try:
        numero = int(input("Ingrese el número del cual desea la tabla de multiplicar: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

print(f"\nTabla de multiplicar del {numero} (hasta 10):")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    

# 37. Realizar un Programa que permita visualizar en pantalla los múltiplos de 5 
# hasta el número 100. 
print("Los múltiplos de 5 son:")

for i in range(5, 101, 5):
    print(i, end=" ")
print("\n(Fin de la lista)")


# 38. Programa que permita determinar si un estudiante que recibe 15 notas gana 
# o no la materia de Programación De Software. Se gana si el promedio es >= 4.0.
NUM_NOTAS = 15
NOTA_MINIMA_APROBAR = 4.0
suma_notas = 0

for i in range(1, NUM_NOTAS + 1):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i}/{NUM_NOTAS} (ej. 4.5): "))
            if 0.0 <= nota <= 5.0:
                suma_notas += nota
                break
            else:
                print("La nota debe estar entre 0.0 y 5.0. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número decimal o entero.")

promedio = suma_notas / NUM_NOTAS

print(f"\nResumen:")
print(f"Promedio obtenido: {promedio:.2f}")

# Condición para determinar si gana o no
if promedio >= NOTA_MINIMA_APROBAR:
    print(f"¡Felicidades! Gana la materia. (Promedio >= {NOTA_MINIMA_APROBAR})")
else:
    print(f"No gana la materia. Debe obtener un promedio de al menos {NOTA_MINIMA_APROBAR} para aprobar.")



# 39. Programa que encuentre el resultado de la operación potencia donde el 
# usuario ingresa la base y el exponente. 
base = 0.0
while True:
    try:
        base = float(input("Ingrese el valor de la base: "))
        break
    except ValueError:
        print("Entrada inválida. Ingrese un número para la base.")

exponente = 0
while True:
    try:
        exponente = int(input("Ingrese el valor entero del exponente: "))
        break
    except ValueError:
        print("Entrada inválida. Ingrese un número entero para el exponente.")

resultado = 1.0 

if exponente == 0:
    resultado = 1.0

elif exponente < 0:
    temp_exponente = -exponente
    contador = 0
    resultado_parcial = 1.0

    while contador < temp_exponente:
        resultado_parcial *= base
        contador += 1

    if resultado_parcial != 0:
        resultado = 1.0 / resultado_parcial
    else:
        print("Error: El resultado es infinito (base cero con exponente negativo).")
        resultado = float('inf')

else:
    contador = 0
    while contador < exponente:
        resultado *= base
        contador += 1

print(f"\nEl resultado de {base} elevado a la {exponente} es: {resultado:.4f}")


# 40. Programa que calcule la suma de los N primeros números naturales, donde N 
# es un número digitado por el usuario. 
N = 0

while True:
    try:
        N = int(input("Ingrese el número N (hasta donde sumar): "))
        if N < 1:
            print("N debe ser un número natural positivo (mayor o igual a 1).")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

suma = 0
contador = 1

while contador <= N:
    suma += contador
    contador += 1 

print(f"\nLa suma de los primeros {N} números naturales es: {suma}")



# 41. Programa que reciba un listado de N números ingresados por el usuario
# y luego determine el número mayor y el número menor. 
N = 0
while True:
    try:
        N = int(input("Ingrese la cantidad de números (N) a procesar: "))
        if N <= 0:
            print("N debe ser un número entero positivo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

mayor = None
menor = None

for i in range(1, N + 1):
    while True:
        try:
            numero = float(input(f"Ingrese el número {i}/{N}: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor numérico.")

    if i == 1:
        mayor = numero
        menor = numero
    else:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

print("\n--- Resultados ---")
print(f"Cantidad de números ingresados (N): {N}")
print(f"Número Mayor encontrado: {mayor}")
print(f"Número Menor encontrado: {menor}")



# 42. Programa que permita obtener el cubo, la cuarta y la quinta potencia de
# N números ingresados por el usuario.

N = 0
while True:
    try:
        N = int(input("Ingrese la cantidad de números (N) a procesar: "))
        if N <= 0:
            print("N debe ser un número entero positivo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

for i in range(1, N + 1):
    numero = 0.0
    while True:
        try:
            numero = float(input(f"\nIngrese el número {i}/{N}: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor numérico.")


    cubo = numero ** 3
    cuarta = numero ** 4
    quinta = numero ** 5

    print(f"  Resultados para {numero}:")
    print(f"    Cubo ({numero}^3): {cubo:.4f}")
    print(f"    Cuarta Potencia ({numero}^4): {cuarta:.4f}")
    print(f"    Quinta Potencia ({numero}^5): {quinta:.4f}")
    
    

# 43. Programa que permita ingresar N números y determine cuantas veces aparece
# el mismo número. 
numero_a_buscar = 0.0
while True:
    try:
        numero_a_buscar = float(input("Ingrese el número que desea buscar y contar (el target): "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un valor numérico.")

N = 0
while True:
    try:
        N = int(input("Ingrese la cantidad total de números (N) a evaluar: "))
        if N <= 0:
            print("N debe ser un número entero positivo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

contador_apariciones = 0

for i in range(1, N + 1):
    numero_ingresado = 0.0
    while True:
        try:
            numero_ingresado = float(input(f"Ingrese el número {i}/{N}: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor numérico.")

    if numero_ingresado == numero_a_buscar:
        contador_apariciones += 1

print("\n--- Resultados del Conteo ---")
print(f"El número objetivo a buscar fue: {numero_a_buscar}")
print(f"Cantidad total de números ingresados: {N}")
print(f"El número {numero_a_buscar} apareció {contador_apariciones} veces.")



# 44. Programa que reciba N calificaciones, y luego calcule:
# a) La nota promedio b) La nota mayor c) Si El estudiante pasa o no (Promedio>=40)
N = 0
NOTA_APROBATORIA = 40

while True:
    try:
        N = int(input("Ingrese la cantidad de notas (N) a procesar: "))
        if N <= 0:
            print("N debe ser un número entero positivo.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

suma_notas = 0
nota_mayor = -1 # Se inicializa en un valor imposible (o muy bajo)

for i in range(1, N + 1):
    nota = 0.0
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i}/{N} (escala 0-100): "))
            if 0.0 <= nota <= 100.0:
                break
            else:
                print("La nota debe estar entre 0 y 100. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor numérico.")

    suma_notas += nota
    if nota > nota_mayor:
        nota_mayor = nota

promedio = 0.0
if N > 0:
    promedio = suma_notas / N

print("\n--- Resultados del Estudiante ---")
print(f"a) Nota Promedio: {promedio:.2f}")
print(f"b) Nota Mayor: {nota_mayor:.2f}")

print("c) Estado de la Materia:")
if promedio >= NOTA_APROBATORIA:
    print(f"   -> ¡APROBADO! (Promedio {promedio:.2f} >= {NOTA_APROBATORIA})")
else:
    print(f"   -> REPROBADO. (Promedio {promedio:.2f} < {NOTA_APROBATORIA})")
    
    

# 45. Programa que permita calcular el factorial de un número. 
# El factorial corresponde a la multiplicación de todos los números naturales 
# anteriores incluyendo el número ingresado. 
numero = -1

while True:
    try:
        numero = int(input("Ingrese un número entero no negativo para calcular su factorial: "))
        if numero < 0:
            print("El factorial solo está definido para números enteros no negativos.")
            continue
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

factorial = 1

if numero > 0:
    for i in range(1, numero + 1):
        factorial *= i

print("\n--- Resultado ---")
print(f"El factorial de {numero} es: {factorial}")