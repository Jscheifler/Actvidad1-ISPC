#Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje.
letra_1 = input("Ingresa la Primera letra: ")
letra_2 = input("Ingresa la Segunda letra: ")

if letra_1 == letra_2:
    print("Las letras son iguales :).")
else:
    print("Las letras NO son iguales :(.")
    
#Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla.
palabra_1 = input("Ingrese la Primera palabra: ")
palabra_2 = input("Ingrese la Segunda palabra: ")

if palabra_1 == palabra_2:
    print("Las palabras son iguales.")
else:
    print("Las palabras NO son iguales.")
    
#Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.
genero = input("Ingrese su género ('f' para femenino, 'm' para masculino): ")

if genero == 'f':
    print("Usted debe votar en la mesa femenina.")
elif genero == 'm':
    print("Usted debe votar en la mesa masculina.")
else:
    print("Género no válido. Por favor, ingrese 'f' o 'm'.")

#Realice un programa que lea dos números y diga cuál es el mayor.
numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))

if numero_1 > numero_2:
    print("El primer número es mayor:", numero_1)
elif numero_2 > numero_1:
    print("El segundo número es mayor:", numero_2)
else:
    print("Los números son iguales.")
#Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.
print("Hola, este es el conversor de monedas")
opciones = input("Seleccione la opción a conversión:\n1. De Pesos a Dólares\n2. De Dólares a Pesos\n")

if opciones == "1":
    pesos = float(input("Ingrese la cantidad de pesos: "))
    tipo_cambio = float(input("Ingrese el tipo de cambio actual: "))
    dolares = pesos / tipo_cambio
    print(f"USD {dolares:.2f}")
elif opciones == "2":
    dolares = float(input("Ingrese la cantidad de dólares: "))
    tipo_cambio = float(input("Ingrese el tipo de cambio actual: "))
    pesos = dolares * tipo_cambio
    print(f"ARS {pesos:.2f}")
else:
    print("ERROR Numero invalido por favor, seleccione 1 o 2.")

#Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.
edad = int(input("Ingrese su edad: "))

if edad >= 16:
    print("Ya puede votar.")
else:
    print("Es menor de 16 para votar, no puede.")
