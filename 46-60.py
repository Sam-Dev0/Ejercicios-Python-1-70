
#46. Problema

n = int(input("¿Cuántos productos va a ingresar? "))
total = 0

for i in range(n):
    precio = float(input("precio del producto: "))
    total += precio

print("Total:", total)


#47. Problema

n = int(input("¿Cuántos estudiantes? "))
mayor = 0

for i in range(n):
    est = float(input("estatura en cm: "))
    if est > mayor:
        mayor = est

print("La mayor estatura es:", mayor, "cm")


#48. Problema

opcion = 0
a = b = 0

while opcion != 6:
    print("\n1. Ingresar 2 números")
    print("2. Sumar")
    print("3. Restar")
    print("4. Multiplicar")
    print("5. Dividir")
    print("6. Salir")

    opcion = int(input("opción: "))

    if opcion == 1:
        a = float(input("primer número: "))
        b = float(input("segundo número: "))
    elif opcion == 2:
        print("Suma:", a + b)
    elif opcion == 3:
        print("Resta:", a - b)
    elif opcion == 4:
        print("Multiplicación:", a * b)
    elif opcion == 5:
        if b != 0:
            print("División:", a / b)
        else:
            print("No se puede dividir entre 0 pendejo")


#49. Problema

opcion = 0

while opcion != 3:
    print("\n1. Factorial (for)")
    print("2. Potencia (while)")
    print("3. Salir")
    opcion = int(input("opción: "))

    if opcion == 1:
        n = int(input("Número para factorial: "))
        fac = 1
        for i in range(1, n+1):
            fac *= i
        print("Factorial:", fac)

    elif opcion == 2:
        base = float(input("Base: "))
        exp = int(input("Exponente: "))
        cont = 1
        pot = 1
        while cont <= exp:
            pot *= base
            cont += 1
        print("Potencia:", pot)


#50. Problema

opcion = 0

while opcion != 4:
    print("\n1. pares hasta 100")
    print("2. de 4 hasta 100 (while)")
    print("3. Tabla de multiplicar")
    print("4. Salir")
    opcion = int(input("opción: "))

    if opcion == 1:
        for i in range(0, 101, 2):
            print(i)

    elif opcion == 2:
        i = 0
        while i <= 100:
            print(i)
            i += 4

    elif opcion == 3:
        n = int(input("Número: "))
        for i in range(1, 11):
            print(n, "x", i, "=", n*i)


#51. Problema

edades = []

for i in range(10):
    edad = int(input("edad: "))
    edades.append(edad)

print(edades)


#52. Problema

nombres = []

for i in range(15):
    nombre = input("nombre: ")
    nombres.append(nombre)

print(nombres)


#53. Problema

valores = []
suma = 0

for i in range(12):
    num = float(input("Ingrese un número: "))
    suma += num

print("Suma total:", suma)


#54. Problema

vector = []
pos = neg = ceros = 0

for i in range(20):
    num = float(input("Número: "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        ceros += 1

print("Positivos:", pos)
print("Negativos:", neg)
print("Ceros:", ceros)


#55. Problema

vector = []

for i in range(20):
    num = input("Ingrese un valor: ")
    vector.append(num)

while True:
    pos = int(input("¿Qué posición desea ver? (1-20, otro número para salir): "))
    if pos < 1 or pos > 20:
        break
    print("Valor:", vector[pos-1])

#56. Problema

vector = []

for i in range(1, 19):
    valor = float(input(f"Valor {i}: "))
    vector.append(valor)

print("\nVector original:", vector)
print("Vector al revés:", vector[::-1])


#57. Problema

clientes = []
suma = 0.0

for i in range(1, 31):
    c = int(input(f"Clientes atendidos en el día {i}: "))
    clientes.append(c)
    suma += c

print(f"\nTotal de clientes atendidos en el mes: {suma}")


#58. Problema

v1 = []
v2 = []
suma = []
resta = []

for i in range(1, 13):
    valor = float(input(f"Valor {i} del vector 1: "))
    v1.append(valor)

for i in range(1, 13):
    valor = float(input(f"Valor {i} del vector 2: "))
    v2.append(valor)

for i in range(12):
    suma.append(v1[i] + v2[i])
    resta.append(v1[i] - v2[i])

print("\nVector de sumas:", suma)
print("Vector de restas:", resta)


#59. Problema

n = int(input("Ingrese la cantidad de elementos: "))

v = []
cuadrado = []
cubo = []

for i in range(1, n+1):
    num = float(input(f"Número {i}: "))
    v.append(num)
    cuadrado.append(num**2)
    cubo.append(num**3)

print("\nVector original:", v)
print("Cuadrados:", cuadrado)
print("Cubos:", cubo)


#60. Problema

salones = 20
estudiantes = []
total = 0

for i in range(1, salones+1):
    cant = int(input(f"Estudiantes en el salón {i}: "))
    estudiantes.append(cant)
    total += cant

mayor = max(estudiantes)
menor = min(estudiantes)

print(f"\nTotal de estudiantes: {total}")
print(f"Salón con mayor cantidad: {estudiantes.index(mayor)+1} ({mayor} estudiantes)")
print(f"Salón con menor cantidad: {estudiantes.index(menor)+1} ({menor} estudiantes)")
