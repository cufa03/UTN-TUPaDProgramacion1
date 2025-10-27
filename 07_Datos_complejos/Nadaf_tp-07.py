# 1) Dado el diccionario precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300

# precios_frutas = {"Banana": 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# precios_frutas["Naranja"]= 1200
# precios_frutas["Manzana"]= 1500
# precios_frutas["Pera"]= 2300
# print (precios_frutas)

#------------------------------------------------------------------------------------------------------------

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800

# precios_frutas["Banana"]= 1330
# precios_frutas["Manzana"]= 1700
# precios_frutas["Melón"]= 2800
# print (precios_frutas)

#------------------------------------------------------------------------------------------------------------

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

# print(precios_frutas.keys())

#------------------------------------------------------------------------------------------------------------

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.

# contactos = {}
# for i in range(5):
#   nombre = input("Ingrese nombre de contacto:")
#   numero = int(input("Ingrese numero de contacto:"))
#   contactos[nombre]=numero
# buscarNombre = input("Ingrese nombre de contacto a buscar: ")
# if contactos[buscarNombre]:
#   print(f"El numero de contacto de {buscarNombre} es: {contactos[buscarNombre]}")
# else:
#   print("El contacto ingresado no existe")

#------------------------------------------------------------------------------------------------------------

# 5) Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra.

# frase = input("Ingrese frase: ")
# palabras = frase.split()
# palabras_unicas = set(palabras)
# diccionario = {}
# for palabra in palabras:
#   if palabra in diccionario:
#     diccionario[palabra] += 1
#   else:
#     diccionario[palabra] = 1
# print("Palabras unicas (set):", palabras_unicas)
# print("Diccionario de palabras y su repetición:", diccionario)

#------------------------------------------------------------------------------------------------------------

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

# alumnos = {}
# for i in range(3):
#     nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
#     notas = []
#     for j in range(3):
#       nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
#       notas.append(nota)
#     notas = tuple(notas)
#     promedio = sum(notas) / len(notas)
#     alumnos[nombre] = tuple(notas)
# print("----- Promedios de los alumnos -----")
# print(alumnos)
# for nombre, notas in alumnos.items():
#     promedio = sum(notas) / len(notas)
#     print(f"{nombre}: {notas}, Promedio = {promedio:.2f}")

#------------------------------------------------------------------------------------------------------------

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# parcial1 = {10, 5, 8}
# parcial2 = {10, 8, 9}
# print(parcial1)
# print(parcial2)
# ambosAprobados = parcial1 & parcial2
# unoSoloAprobado = parcial1 ^ parcial2
# almenosUnoAprobado = parcial1 | parcial2
# print("Aprobo ambos parciales: ", ambosAprobados)
# print("Aprobo un solo parcial: ", unoSoloAprobado)
# print("Aprobo al menos 1 parcial: ", almenosUnoAprobado)

#------------------------------------------------------------------------------------------------------------

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.

# almacen = {
#   "leche":5,
#   "azucar":7,
#   "sal":10
# }
# print("Almacen actual:", almacen)
# producto = input("Ingrese su producto: ")
# cantidad = int(input("Ingrese cantidad a almacenar: "))
# if producto in almacen:
#   almacen[producto] += cantidad
# else:
#   almacen[producto] = cantidad
# print("El almacen actualizado:", almacen)

#------------------------------------------------------------------------------------------------------------

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# agenda = {
#     ("lunes", "10:00"): "Reunión",
#     ("martes", "15:00"): "Clase de inglés"
# }
# while True:
#     print("\n--- MENÚ AGENDA ---")
#     print("1. Consultar evento")
#     print("2. Agregar evento")
#     print("3. Ver toda la agenda")
#     print("4. Salir")
#     opcion = input("Seleccione una opción: ")
#     if opcion == "1":
#       dia = input("Ingrese el día: ").lower()
#       hora = input("Ingrese la hora (el formato es: 'hh:mm'): ")
#       clave = (dia, hora)
#       if clave in agenda:
#           print(f"Evento: {agenda[clave]}")
#       else:
#           print("No tienes ningun evento en ese día y hora.")
#     elif opcion == "2":
#       dia = input("Ingrese el día: ").lower()
#       hora = input("Ingrese la hora (el formato es: 'hh:mm'): ")
#       evento = input("Ingrese el evento: ")
#       clave = (dia, hora)
#       agenda[clave] = evento
#       print(f"Evento: {evento}, agregado con éxito.")
#     elif opcion == "3":
#       print("\nAGENDA DE EVENTOS:")
#       for (dia, hora), evento in agenda.items():
#           print(f"{dia} a las {hora}: {evento}")
#     elif opcion == "4":
#       print("Saliendo de la agenda...")
#       break
#     else:
#       print("Opción inválida. Intente nuevamente.")

#------------------------------------------------------------------------------------------------------------

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.
# original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
# invertido = {}
# for clave in original:
#   print(f"Clave: {clave}, Valor: {original.get(clave)}")
#   invertido[original.get(clave)] = clave
# print("Diccionario original: ", original)
# print("Diccionario invertido: ", invertido)