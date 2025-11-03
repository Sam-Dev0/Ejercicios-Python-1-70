#16
n1 = int(input('ingrese el primer numero: '))
n2 = int(input('ingrese el segundo numero: '))

if n1 == n2:
    print(n1-n2)
else:
    print(n1+n2)

#17
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

#18
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


#19
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

#20
n = int(input('digite un numero: '))
if n > 0 and n % 2 == 0:
  print("El numero es par")
else:
  print("El numero es impar")

#21
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
    

#22

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



#23
edad = int(input('digite la edad: '))
estatura = float(input('digite la estatura: '))
peso = int = int(input('digite el peso: '))
if edad <= 18 and estatura >= 1.80 and peso < 80:
    print('Aceptado')
else:
    print('no aceptado')

#24

letra = input("Ingrese une letra: ").lower()
         
match letra:
    case "a" "e" "i" "o" "u":
        print(f"La letra '{letra}' es una que termina por vocal")
    case _: 
        print(f"La letra '{letra}' no termina en una vocal")


#25

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
    
#26    
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


#28
for numero in range(0, 1001):
    print(numero, end=' ')
print("\n" + "-"*40)


#29
for par in range(0, 201, 2):
    print(par, end=' ')
print("\n" + "-"*40)


#30
for impar in range(201, 500, 2):
    print(impar, end=' ')
print("\n" + "-"*40)