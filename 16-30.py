#16 Programa en el cual se ingresen 2 números y luego realice las siguientes operaciones: 
# a) Si los números son iguales restarlos 
# b) Si los números son diferentes sumarlos
n1 = int(input('ingrese el primer numero: '))
n2 = int(input('ingrese el segundo numero: '))

if n1 == n2:
    print(n1-n2)
else:
    print(n1+n2)
    

#17 Programa en el cual reciba como entradas la siguiente información: Código del Estudiante, Nombre del Estudiante, 
# Nombre de la Materia y Tres Notas de 1.0 a 5.0. Con esta información el programa debe calcular la nota definitiva (promedio) y determinar si el estudiante aprueba o no la materia
#(Definitiva mayor a 4.0). Debe imprimir coma salidas el nombre, el código, la materia y si aprobó o no.
id = int(input('digite el id del estudiante: '))
mat = input('digite la materia: ')
nom = input('digite el nombre del estudiante: ')
n1 = float(input('digite la primera nota: '))
n2 = float(input('digite la segunda nota: '))
n3 = float(input('digite la tercera nota: '))
sum = n1 + n2 + n3 
resultado = sum / 3

if sum > 3.0:
    print(f'el estudiante {nom} perdio la materia {mat} con {resultado}')
elif sum <= 3.0:
    print(f'{id} el estudiante {nom} gano la materia {mat} con {resultado}')
    

#18 Programa para determinar cuánto pagara una persona por una compra de la cual se sabe la cantidad de artículos y el valor unitario. 
# Se debe tener en cuenta que el almacén hace un 20% de descuento cuando la compra supera $100000.
articulos = int(input('digite la cantidad de los articulos: '))
cantidad = int(input('digite el valor del articulo: '))
total = cantidad * articulos
total_pagar = total

if total >= 100000:
    descuento = total * 0.20
    total_pagar = total - descuento
    print('tiene un descuento del 20% y le queda en {total_pagar}')
else:
    print('el total de la compra es de {total}')


#19 Programa que permita determinar el total a pagar por una compra del la cual se sabe el valor unitario y la cantidad. 
# Se debe tener en cuanta que se realiza un descuento del 15% por compra inferiores a $20000 y del 35% por compras mayores o iguales a $20000.
articulos = int(input('digite la cantidad de los articulos: '))
cantidad = float(input('digite el valor del articulo: '))
total = cantidad * articulos

if total < 20000:
    descuento = total * 0.15
    total_pagar = total - descuento
    print(f'tiene un descuento del 15% y le queda en {total_pagar}')
elif total >= 20000:
    descuento = total * 0.35
    total_pagar = total - descuento
    print('tiene un descuento del 35% y le queda en {total_pagar}')
    

#20 Programa para determinar si un número cualquiera ingresado por el usuario es par o impar.(Usar operación Modulo)
n = int(input('digite un numero: '))
if n > 0 and n % 2 == 0:
  print("El numero es par")
else:
  print("El numero es impar")
    

#21 Programa el cual permita ingresar los valores de temperatura de cada día durante una semana. Le programa debe calcular la temperatura promedio y luego mostrar los siguientes mensajes: 
# a) Si el promedio es mayor a 35° mostrar el mensaje “Que semana tan calurosa”
# b) Si el promedio esta entre 15° y 35° mostrar el mensaje “Que clima tan delicioso” 
# c) Si el promedio es menor de 15° mostrar el mensaje “Que semana tan fría”
lunes = float(input('digite la temperatura del lunes: '))
martes = float(input('digite la temperatura del martes: '))
miercoles = float(input('digite la temperatura del miercoles: '))
jueves = float(input('digite la temperatura del jueves: '))
viernes = float(input('digite la temperatura del virnes: ')) 
sabado = float(input('digite la temperatura del sabado: '))
domingo = float(input('digite la temperatura del domingo: '))
dias = lunes + martes + miercoles + jueves + viernes + sabado + domingo
promedio = dias / 7
if promedio > 35:
    print(f'la temperatura fue de {promedio} que semana tan calurosa')
elif promedio >= 15 and promedio <= 35:
    print(f'la temperatura fue de {promedio} que clima tan delicioso')
elif promedio < 15:
    print(f'la temperatura fue de {promedio} grados que semana tan fría')
else:
    print('clima no valido')
    

#22 Programa que permita calcular el valor final a pagar en una súper tienda en donde se aplican los siguientes descuentos: 
# a) Por compras entre 10000 y 20000 el 10% 
# b) Por compras entre 20001 y 50000 el 30% 
# c) Por compras superiores a 50000 el 50%
compra = float(input("Ingrese el valor total de la compra: "))

if 10000 <= compra <= 20000:
    descuento = compra * 0.10
elif 20001 <= compra <= 50000:
    descuento = compra * 0.30
elif compra > 50000:
    descuento = compra * 0,50
else:
    descuento = 0
total = compra - descuento

print(f"Descuento aplicado: {descuento}")
print(f"Total a pagar: {total}")


#23 Programa para determinar si un deportista es aceptado en el quipo de baloncesto de Bogotá. Las condiciones para ser aceptado son: 
# a) La edad debe ser menor o igual a 18 años 
# b) La estatura debe ser mayor a 180 cm 
# c) El peso debe ser menor o igual a 80 kg
# Si el aspirante cumple las 3 condiciones aceptarlo si no rechazarlo.
edad = int(input('digite la edad: '))
estatura = float(input('digite la estatura: '))
peso = int = int(input('digite el peso: '))
if edad <= 18 and estatura >= 1.80 and peso < 80:
    print('Aceptado')
else:
    print('no aceptado')
    

#24 Programa que permita determinar si una letra es o no vocal
letra = input("Ingrese une letra: ").lower()
         
match letra:
    case "a" "e" "i" "o" "u":
        print(f"La letra '{letra}' es una que termina por vocal")
    case _: 
        print(f"La letra '{letra}' no termina en una vocal")


#25 Programa que permita realizar los siguientes requerimientos: 1. Calcular distancia recorrida 2. Calcular tiempo 3. Calcular velocidad.
# Dependiendo de lo que seleccione el usuario se debe solicitar los datos correspondientes y la operación adecuada, 
# teniendo en cuenta el movimiento rectilíneo uniforme cuya principal ecuación es: X=V*T.
print(1,'calcular distancia')
print(2,'calcular tiempo')
print(3,'calcular velocida')

opcion = int(input('seleccione una opcion 1,2 o 3: '))
valor = 0

if opcion == 1:
    v=float(input('ingrese el valor de la velocidad: '))
    t=float(input('ingrese el valor de el tiempo: '))
    valor = v * t
    print(f'la distancia recorrida es de {valor} metros')
elif opcion == 2:
    d=int(input('ingrese el valor de la distancia: '))
    v=float(input('digite el valor de la velocida: '))
    valor = d / v
    print(f'la velocidad recorrida es de {valor} kilometros')
elif opcion == 3:
    d=int(input('ingrese el valor de la distancia: '))
    t=float(input('digite el valor de el tiempo: '))
    valor = d / t
    print(f'el tiempo recorrida es de {valor} segundos')

     
#26 Programa que permita ingresar un número cualquiera y luego mostrar el siguiente menú:
# 1. Determinar si es positivo o negativo 2. Determinar si es par o impar
# El programa debe realizar las operaciones que el usuario seleccione del menú
numero = int(input("Ingrese un numero: "))

print("Seleccione una opcion :) :")
print("1. Determinar si es positivo o negativo")
print("2. Determinar si es par o impar")

opcion = int(input("Ingrese su opción (1 o 2): "))

match opcion:
    case 1:
        if numero > 0:
            print(f"El numero {numero} es POSITIVO.")
        elif numero < 0:
            print(f"El numero {numero} es NEGATIVO.")
        else:
            print("El numero es CERO.")
    case 2:
        if numero % 2 == 0:
            print(f"El numero {numero} es PAR.")
        else:
            print(f"El numero {numero} es IMPAR.")
    case _:
        print("Opción no válida.")

#27 Programa que muestre un menú que tenga las siguientes opciones:
# 1. Pasa o no la materia? 2. Es mayor o menor de edad?
# Caso 1: Solicitar 3 notas y determinar si el promedio es mayor a 3.0, en ese caso el estudiante pasa.
# Caso 2: Se debe solicitar el año de nacimiento y el año actual y determinar si es o no mayor de edad.
while True:
    print("\n" + "="*30)
    print("**MENÚ DE OPCIONES**")
    print("1. Pasa o no la materia?")
    print("2. Es mayor o menor de edad?")
    print("3. Salir")
    print("="*30)
    
    opcion = input("Seleccione una opción (1, 2 o 3): ")
    
    if opcion == '1':
        print("\n--- Opción 1: Pasa o no la materia ---")
        try:
            nota1 = float(input("Ingrese la nota 1: "))
            nota2 = float(input("Ingrese la nota 2: "))
            nota3 = float(input("Ingrese la nota 3: "))
            
            promedio = (nota1 + nota2 + nota3) / 3
            print(f"El promedio es: {promedio:.2f}")
            
            if promedio > 3.0:
                print("**¡PASA la materia!** 🥳")
            else:
                print("**NO PASA la materia.** 😔")
                
        except ValueError:
            print("Error: Ingrese solo números válidos para las notas.")

    elif opcion == '2':
        print("\n--- Opción 2: Es mayor o menor de edad ---")
        try:
            año_actual = int(input("Ingrese el año actual (ej. 2024): "))
            año_nacimiento = int(input("Ingrese su año de nacimiento (ej. 1990): "))
            
            if año_nacimiento > año_actual:
                print("Error: El año de nacimiento no puede ser futuro.")
                continue 
            
            edad = año_actual - año_nacimiento
            print(f"Su edad es: {edad} años")
            
            if edad >= 18:
                print("**Usted es MAYOR de edad.**")
            else:
                print("**Usted es MENOR de edad.**")
                
        except ValueError:
            print("Error: Ingrese un año válido (número entero).")

    elif opcion == '3':
        print("\n¡Hasta pronto!")
        break

    else:
        print("\nOpción no válida. Por favor, ingrese 1, 2 o 3.")
        

#28 Programa que permita ver los números naturales comprendidos entre 0 y 1000
for numero in range(0, 1001):
    print(numero, end=' ')
print("\n" + "-"*40)


#29 Programa que imprima los pares de entre 0 y 200
for par in range(0, 201, 2):
    print(par, end=' ')
print("\n" + "-"*40)


#30 Programa que imprima los números impares entre 201 y 499
for impar in range(201, 500, 2):
    print(impar, end=' ')
print("\n" + "-"*40)
