#Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")
    
#Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:
importe = float(input("Ingrese el importe: "))
forma_pago = int(input("Ingrese la forma de pago (1: Contado, 2: Tarjeta crédito, 3: Tarjeta débito): "))

descuento = 0
interes = 0

if forma_pago == 1:#Contado se aplica un descuento del 10% al importe
    descuento = importe * 0.1
    importe_total = importe - descuento
elif forma_pago == 2:#Tarjeta crédito se aplica un interés de 10%
    interes = importe * 0.1
    importe_total = importe + interes
elif forma_pago == 3:#Tarjeta débito se aplica un interés de 10%
    descuento = importe * 0.05
    importe_total = importe - descuento
else:
    print("Forma de pago no válida.")
    
print("Importe: $", importe)
print("Descuento: $", descuento)
print("Interés: $", interes)
print("Importe total: $", importe_total)

#Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.
def es_par(numero):
    if numero % 2 == 0:
        return "PAR"
    else:
        return "IMPAR"

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

mayor = num1

if num2 > mayor:
    mayor = num2

if num3 > mayor:
    mayor = num3

print("El número mayor es:", mayor)
print("El número mayor es", es_par(mayor))

#Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.
numero = int(input("Ingrese un número del 1 al 7: "))

if numero == 1:
    dia_semana = "Lunes"
elif numero == 2:
    dia_semana = "Martes"
elif numero == 3:
    dia_semana = "Miércoles"
elif numero == 4:
    dia_semana = "Jueves"
elif numero == 5:
    dia_semana = "Viernes"
elif numero == 6:
    dia_semana = "Sábado"
elif numero == 7:
    dia_semana = "Domingo"
else:
    dia_semana = "Número inválido"

print("El día de la semana correspondiente al número", numero, "es", dia_semana)

#Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.
numero = int(input("Ingrese un número del 1 al 12: "))

if numero == 1:
    mes = "Enero"
elif numero == 2:
    mes = "Febrero"
elif numero == 3:
    mes = "Marzo"
elif numero == 4:
    mes = "Abril"
elif numero == 5:
    mes = "Mayo"
elif numero == 6:
    mes = "Junio"
elif numero == 7:
    mes = "Julio"
elif numero == 8:
    mes = "Agosto"
elif numero == 9:
    mes = "Septiembre"
elif numero == 10:
    mes = "Octubre"
elif numero == 11:
    mes = "Noviembre"
elif numero == 12:
    mes = "Diciembre"
else:
    mes = "Número inválido"

print("El mes correspondiente al número", numero, "es", mes)
