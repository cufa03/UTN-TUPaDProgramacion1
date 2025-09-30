## --- Resolución Trabajo Práctico Nº 6 - Funciones --- ##
# ----------------------------------------------------------------------------------------

## 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# def imprimir_hola_mundo():
#   return ("\nHola mundo!")

# print(imprimir_hola_mundo())

# ----------------------------------------------------------------------------------------

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al suario.

# def saludar_usuario(nombre):
#   return (f"\nHola {nombre}!")

# input = input("Ingrese su nombre: ")
# print(saludar_usuario(input))

# ----------------------------------------------------------------------------------------

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# def informacion_personal(nombre, apellido, edad, residencia):
#   return (f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# nombreUsuario = input("\nIngrese su nombre: ")
# apellidoUsuario = input("Ingrese su apellido: ")
# edadUsuario = input("Ingrese su edad: ")
# residenciaUsuario = input("Ingrese la ciudad donde vive: ")

# print(informacion_personal(nombreUsuario, apellidoUsuario, edadUsuario, residenciaUsuario))

# ----------------------------------------------------------------------------------------

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# def calcular_area_circulo(radio):
#   print(f"\nAREA = {3.14 * (radio**2)}")

# def calcular_perimetro_circulo(radio):
#   print(f"PERIMETRO = {2 * 3.14 * radio}")

# while True:
#   radioUsuario = input("Ingrese el radio del circulo: ")
#   if radioUsuario.isdigit():
#     radioUsuario=int(radioUsuario)
#     break
#   else:
#     print("\nSolo se aceptan numeros enteros mayores a 0")
#     continue

# calcular_area_circulo(radioUsuario)
# calcular_perimetro_circulo(radioUsuario)

# ----------------------------------------------------------------------------------------

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# def segundos_a_horas(segundos):
#   print(f"\n----- Convirtiendo {segundos} segundos a horas -----")
#   print(f"{segundos} equivale a {segundos/3600} horas.")

# while True:
#   inputUsuario = input("Ingrese la cantidad de segundos a convertir: ")
#   if inputUsuario.isdigit():
#     inputUsuario = int(inputUsuario)
#     if inputUsuario < 0:
#       print("El numero debe ser mayor o igual a 0.\n")
#       continue
#     else:
#       print("Numero validado... Calculando...")
#       segundos_a_horas(inputUsuario)
#       break
#   else:
#     print("Debe ingreser un numero entero.")
#     continue

# ----------------------------------------------------------------------------------------

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# def tabla_multiplicar(numero):
#   for i in range(1,11,1):
#     print(f"{numero}x{i} = {numero*i}")

# while True:
#   numeroUsuario = input("Ingrese un numero entero: \n")
#   if numeroUsuario.isdigit():
#     numeroUsuario = int(numeroUsuario)
#     if numeroUsuario > 0:
#       tabla_multiplicar(numeroUsuario)
#       break
#     else:
#       print("El numero debe ser mayor a cero")
#       continue
#   else:
#     print("Solo se aceptan numeros positivos...")
#     continue

# ----------------------------------------------------------------------------------------

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

# def operaciones_basicas(a, b):
#     return (a+b, a-b, a*b, a/b)

# # Uso de la función
# num1 = 5
# num2 = 2
# resultados = operaciones_basicas(num1, num2)

# print(f"\nSuma {num1}+{num2}: {resultados[0]}")
# print(f"Resta {num1}-{num2}: {resultados[1]}")
# print(f"Multiplicación {num1}*{num2}: {resultados[2]}")
# print(f"División {num1}/{num2}: {resultados[3]}")

# ----------------------------------------------------------------------------------------

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# def calcular_imc(peso, altura):
#   imc = peso / (altura ** 2)
#   return imc

# pesoUsuario = float(input("\nIngrese su peso en kilogramos (Ejemplo: 74): "))
# alturaUsuario = float(input("Ingrese su altura en metros (Ejemplo: 1.80): "))
# print(f"\nSu IMC es: {calcular_imc(pesoUsuario, alturaUsuario):.2f}")

# ----------------------------------------------------------------------------------------

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# def celsius_a_fahrenheit(celsius):
#   far = celsius * 9/5 + 32
#   print(f"Temperatura en Fahrenheit: {far}")

# while True:
#   inputUsuario = input("Ingrese temperatura en celsius a convertir: ")
#   if inputUsuario.isdigit():
#     inputUsuario = float(inputUsuario)
#     celsius_a_fahrenheit(inputUsuario)
#     break
#   else:
#     print("Caracter invalido... son validos los números")
#     continue

# ----------------------------------------------------------------------------------------

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# def calcular_promedio(a, b, c):
#   prom = ((a+b+c)/3)
#   print(f"El promedio de las notas ({a}, {b}, {c}) es: {prom:.2f}")

# while True:
#   num1 = input("Ingrese la primer nota: ")
#   num2 = input("Ingrese la segunda nota: ")
#   num3 = input("Ingrese la tercer nota: ")
#   if num1.isdigit() and num2.isdigit() and num3.isdigit():
#     num1 = float(num1)
#     num2 = float(num2)
#     num3 = float(num3)
#     if num1 >= 0 and num2 >= 0 and num3 >= 0:
#       calcular_promedio(num1,num2,num3)
#       break
#     else:
#       print("Solo numeros positivos...")
#       continue
#   else:
#     print("Caracter invalido... son validos los números")
#     continue