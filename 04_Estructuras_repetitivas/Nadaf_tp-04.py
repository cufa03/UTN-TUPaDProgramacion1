# --- Resolucion Trabajo Practico Nº 4 - Estructuras Repetititvas ---
# ----------------------------------------------------------------------------------------
# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

# for i in range (0, 101, 1):
#   print(i)

# ----------------------------------------------------------------------------------------

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

# num = input("Ingrese un número entero: ")
# cantDigitos = 0
# for digitos in num:
#   cantDigitos = cantDigitos + 1
# print("La cantidad de digitos del número ingresado es:", cantDigitos)

# ----------------------------------------------------------------------------------------

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# num1 = int(input("Ingrese el comienzo del rango: "))
# num2 = int(input("Ingrese el final del rango: "))
# inicio = 0
# fin = 0
# acum = 0
# if num1 > num2:
#   inicio = num2
#   fin = num1
# elif num2 > num1:
#   inicio = num1
#   fin = num2
# else:
#   print("Por favor ingrese 2 valores enteros distintos")

# for i in range(inicio+1, fin, 1):
#     acum = acum + i

# print("El resultado de la suma de todos los enteros comprendidos dentro del rango es:", acum)

# ----------------------------------------------------------------------------------------

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# acum = 0
# num = int(input("Ingrese un número entero: "))
# while num != 0:
#   acum = acum + num
#   num = int(input("Ingrese un número entero (0 para salir): "))

# print("El resultado de la suma de todos los números ingresados es:", acum)

# ----------------------------------------------------------------------------------------

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# import random
# intentos = 0
# inputUsuario = int(input("Adivina el número aleatorio entre 0 y 9: "))
# num = random.randint(0,9)
# print(num)
# while inputUsuario != num:
#   intentos = intentos + 1
#   inputUsuario = int(input("Vuelva a intentarlo: "))

# print(f"Muy bien! adivino el número en {intentos} intentos.")

# ----------------------------------------------------------------------------------------

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

# print("Lista de números pares del 100 al 0")
# for i in range(100, 0, -1):
#   if (i % 2 == 0):
#     print(i)

# ----------------------------------------------------------------------------------------

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# num = int(input("Ingrese un número entero positivo, para mostrar la suma desde 0 hasta ese número: "))
# suma = 0
# for i in range(0, num+1, 1):
#   suma = suma + i

# print(f"La suma de todos los números comprendidos entre 0 y {num} es: {suma}")

# ----------------------------------------------------------------------------------------

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# par = 0
# impar = 0
# pos = 0
# neg = 0
# num = 0
# for i in range(0, 101, 1):
#   num = int(input("Ingrese un valor positivo o negativo pero entero: "))
#   if num > 0:  
#     if num % 2 == 0:
#       par = par + 1
#     else:
#       impar = impar + 1
#     pos = pos + 1
#   elif num < 0:
#     if num % 2 == 0:
#       par = par + 1
#     else:
#       impar = impar + 1
#     neg = neg + 1

# print("Números pares: ", par)
# print("Números impares: ", impar)
# print("Números positivos: ", pos)
# print("Números negativos: ", neg)

# ----------------------------------------------------------------------------------------

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

# from statistics import mean
# rango=[]
# num = 0
# for i in range(0,101,1):
#   num = int(input("Ingrese un números entero: "))
#   rango.append(num)
# media = mean(rango)
# print(f"La media de los números ingresados es: {media}")

# ----------------------------------------------------------------------------------------

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# numero = list(input("Ingrese un número: "))
# numero.reverse()
# numero_invertido = "".join(numero)
# print("El número invertido es:", numero_invertido)