#1
n = 1
j = 2
print(n+j)

#2
numeros = 3*7*2
print(numeros)

#3
v = 80
t = 15
distancia = v*t
print(f'la distancia es de {distancia} metros')

#4
año = 2025
año_nacimineto = 2007
edad = año - año_nacimineto
print(f'usted tiene {edad} años')

#5
numero = int(input('digite el numero para calcular su 20%: '))
porcentaje = numero * 0.20
print(f'el 20 %  {numero} es de {porcentaje}')

#6
print(1,'30%')
print(2,'60%')
print(3,'90%')

opcion = int(input('seleccione una opcion: '))
valor = int(input('ingrese el valor: '))

if opcion == 1:
    resultado = valor * 0.30
    print(f'el 30% de {valor} es {resultado}')
elif opcion == 2:
    resultado = valor * 0.60
    print(f'el 60% de {valor} es {resultado}')
elif opcion == 3:
    resultado = valor * 0.90
    print(f'el 90% de {valor} es {resultado}')
    
#7
lado1 = 5
lado2 = 5
area = lado1 * lado2
print(f'el area del cuadrado es de {area}')

#8
num1 = 3
num2 = 6
num3 = 10
promedio = (num1 + num2 + num3) / 3 
print('el promedio es de {promedio}')

#9
producto = 'tomate'
valoruni = 500
cantidad = 3
iva = 240.00
total = 1500 + iva
print(producto)
print(valoruni)
print(cantidad)
print(f'el total a pagar es de {total}')

#10
salario_diario = 80000
dias_trabajados = 25
salario_total = salario_diario * dias_trabajados 
salario_mensual = salario_total - 200000 - 270000
print(f'su salario mensual es de {salario_mensual}')

#11
año = 2025
año_nacimineto = 2007
edad = año - año_nacimineto
if edad >= 18:
    print('es mayor de edad')
else:
    print('es menor de edad') 

#12
n = 4
if n > 0:
  print("El numero es positivo")
else:
  print("El numero es negativo")

#13
n1 = int(input('ingrese el primer numero: '))
n2 = int(input('ingrese el segundo numero: '))
if n1 > n2:
  print("El numero", n1,"es mayor")
else:
  print("el numero", n2,"es mayor")
  
#14
grado = 6
if grado >= 6:
    print('requiere refrigerio')
else:
    print('no requiere refrigerio')

#15
numero = int(input('ingrese un numero: '))
resultado = numero / 2
if resultado <= 100:
    print('es menor que 100')
else:
    print('el es mayor que 100')