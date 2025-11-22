#61. Problema

nombres = []
apellidos = []

for i in range(1, 26):
    nombre = input(f"Nombre {i}: ")
    nombres.append(nombre)

for i in range(1, 26):
    apellido = input(f"Apellido {i}: ")
    apellidos.append(apellido)

print("\nListado completo:")
for i in range(25):
    print(f"{nombres[i]} {apellidos[i]}")


#62. Problema
filas = int(input("número de filas: "))
columnas = int(input("número de columnas: "))

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"valor para la posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

print("\nContenido de la matriz con posiciones:")
for i in range(filas):
    for j in range(columnas):
        print(f"Matriz[{i}][{j}] = {matriz[i][j]}")


#63. Problema

matriz = []
suma_total = 0

for i in range(3):
    fila = []
    for j in range(4):
        valor = int(input(f"valor para [{i}][{j}]: "))
        suma_total += valor
        fila.append(valor)
    matriz.append(fila)

print("\nLa matriz es:")
for fila in matriz:
    print(fila)

print("\nSuma total:", suma_total)
print("Promedio:", suma_total / 12)


#64. Problema

filas = int(input("número de filas: "))
columnas = int(input("número de columnas: "))

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"valor en [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

while True:
    f = int(input("\nFila a consultar: "))
    c = int(input("Columna a consultar: "))

    if f >= filas or c >= columnas:
        print("Fin del programa PIPIPI.")
        break
    else:
        print(f"Valor en [{f}][{c}] = {matriz[f][c]}")


#65. Problema

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))

matriz = []
pos = neg = ceros = 0

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"valor en [{i}][{j}]: "))
        fila.append(valor)
        if valor > 0:
            pos += 1
        elif valor < 0:
            neg += 1
        else:
            ceros += 1
    matriz.append(fila)

print("\nPositivos:", pos)
print("Negativos:", neg)
print("Ceros:", ceros)


#66. Problema

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Valor [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

buscar = int(input("\nValor a buscar: "))
encontrado = False

for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] == buscar:
            print(f"Encontrado en posición [{i}][{j}]")
            encontrado = True

if not encontrado:
    print("no está en la matriz.")


#67. Problema

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(int(input(f"Valor [{i}][{j}]: ")))
    matriz.append(fila)

print("\nSuma de filas:")
for i in range(filas):
    print(f"Fila {i} = {sum(matriz[i])}")


#68. Problema

filas = int(input("Filas: "))
columnas = int(input("Columnas: "))

matriz = []

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(int(input(f"Valor [{i}][{j}]: ")))
    matriz.append(fila)

print("\nSuma de columnas:")
for j in range(columnas):
    suma = 0
    for i in range(filas):
        suma += matriz[i][j]
    print(f"Columna {j} = {suma}")


#69. Problema

matriz = []
suma = 0

for i in range(5):
    fila = []
    for j in range(5):
        valor = int(input(f"Valor [{i}][{j}]: "))
        fila.append(valor)
        if i == j:
            suma += valor
    matriz.append(fila)

print("\nSuma diagonal principal:", suma)


#70. Problema

matriz = []
arriba = 0
abajo = 0

for i in range(5):
    fila = []
    for j in range(5):
        valor = int(input(f"Valor [{i}][{j}]: "))
        fila.append(valor)
        if j > i:
            arriba += valor
        elif j < i:
            abajo += valor
    matriz.append(fila)

print("\nSuma valores ARRIBA de la diagonal:", arriba)
print("Suma valores ABAJO de la diagonal:", abajo)
