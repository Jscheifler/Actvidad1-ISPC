#Realice un programa que lea 4 números y diga cuántos son pares y cuántos impares y devuelva la sumatoria de los pares

def contar_pares_impares(nums):
    pares = 0
    impares = 0
    sumatoria_pares = 0

    for num in nums:
        if num % 2 == 0:
            pares += 1
            sumatoria_pares += num
        else:
            impares += 1

    return pares, impares, sumatoria_pares


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))

numeros = [num1, num2, num3, num4]

pares, impares, sumatoria_pares = contar_pares_impares(numeros)

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Sumatoria de los números pares:", sumatoria_pares)

#Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.
cantidad_mayores = 0
cantidad_menores = 0
numero_maximo = float('-inf')
numero_minimo = float('inf')

for ingresado in range(10):
    numero = float(input(f"Ingrese el número {ingresado+1}: "))

    if numero > numero_maximo:
        numero_maximo = numero

    if numero < numero_minimo:
        numero_minimo = numero

    if numero > 100:
        cantidad_mayores += 1
    elif numero < 100:
        cantidad_menores += 1

print("Cantidad de números mayores a 100:", cantidad_mayores)
print("Cantidad de números menores a 100:", cantidad_menores)
print("Número máximo:", numero_maximo)
print("Número mínimo:", numero_minimo)

#Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.

contador_mujeres = 0
contador_varones = 0
contador_mayores = 0
contador_menores = 0

for ingresado in range(15):
    edad = int(input(f"Ingrese la edad de la persona {ingresado+1}: "))
    sexo = input(f"Ingrese el sexo de la persona {ingresado+1} (M/F): ")

    if sexo.upper() == "M":
        contador_varones += 1
    elif sexo.upper() == "F":
        contador_mujeres += 1

    if edad >= 18:
        contador_mayores += 1
    else:
        contador_menores += 1

print("Cantidad de mujeres:", contador_mujeres)
print("Cantidad de varones:", contador_varones)
print("Cantidad de personas mayores de edad:", contador_mayores)
print("Cantidad de personas menores de edad:", contador_menores)

#Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

sumatoria_positivos = 0

for ingresado in range(10):
    numero = float(input(f"Ingrese el número {ingresado+1}: "))

    if numero > 0:
        print(numero)
        sumatoria_positivos += numero

print("Sumatoria de los números positivos:", sumatoria_positivos)

#Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.
for ingresado in range(15):
    numero = float(input(f"Ingrese el número negativo {ingresado+1}: ")) # F Es una f-string (cadena formateada) que permite insertar el valor de la variable suma dentro del mensaje.

    numero_positivo = abs(numero)  # Utilizamos la función abs() para obtener el valor absoluto del número

    print("Número positivo:", numero_positivo)
 