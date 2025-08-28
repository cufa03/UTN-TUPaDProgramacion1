# Resolucion Trabajo Practico 3

# -------------------------------------------------------------------

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

# edad = int(input("Ingrese su edad: "))
# if (edad > 18):
#   print("Es mayord de edad")
# else:
#   print("No es mayor de 18 años...")

# -------------------------------------------------------------------

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

# nota = int(input("Ingrese la nota obtenida: "))
# if (nota >= 6):
#   print("Aprobado")
# else:
#   print("Desaprobado")

# -------------------------------------------------------------------

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

# numero = int(input("Ingrese un numero par: "))
# if (numero % 2 == 0):
#   print("Ha ingresado un número par")
# else:
#   print("Por favor, ingrese un número par")
  
# -------------------------------------------------------------------

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

# edad = int(input("Ingrese su edad: "))
# if (edad < 0):
#   print("Porfavor ingrese un numero mayor a 0")
# elif (edad < 12):
#   print("Categoria Niño/a...")
# elif (edad >= 12 and edad < 18):
#   print("Categoria Adolescente...")
# elif (edad >= 18 and edad < 30):
#   print("Categoria Adulto/a joven...")
# else: print("Adulto/a")

# -------------------------------------------------------------------

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

# print("Recuerde que la contraseña debe tener entre 8 y 14 caracteres")
# contraseña = input("Ingrese su contraseña: ")
# if ( 8 < len(contraseña) < 14):
#   print("Ingreso una contraseña de logitud adecuada")
# else:
#   print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres...")

# -------------------------------------------------------------------

# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#   ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
#   ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
#   ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Definir la lista numeros_aleatorios de la siguiente forma: 
#   import random 
#   numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria.

# from statistics import mode, median, mean
# import random 
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# moda = mode(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# media = mean(numeros_aleatorios)
# if(media > mediana and mediana > moda):
#   print("Sesgo positivo")
#   print("La media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.")
# elif(media < mediana and mediana < moda):
#   print("Sesgo negativo")
#   print("La media es menor que la mediana y, a su vez, la mediana es menor que la moda.")
# else:
#   print("Sin sesgo")
#   print("La media, la mediana y la moda son iguales.")

# -------------------------------------------------------------------

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

# palabra = input("Ingrese una palabra o frase: ")
# if palabra[-1] == "a" or palabra[-1] == "e" or palabra[-1] == "i" or palabra[-1] == "o" or palabra[-1] == "u":
#     palabra = palabra + "!"
#     print(palabra)
# else:
#     print(palabra)

# -------------------------------------------------------------------

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

# nombre = input("Ingrese su nombre: ")
# print("Opcion 1 --> Si quiere su nombre en mayúsculas.")
# print("Opcion 2 --> Si quiere su nombre en minúsculas.")
# print("Opcion 3 --> Si quiere su nombre con la primera letra mayúscula.")
# opcion = int(input("Seleccione una opcion para continuar: "))
# print("Ingrese solo opcion 1, 2 o 3, no es valido otro valor")
# if (opcion == 1):
#   print(f"Nombre: {nombre.upper()}")
# elif (opcion == 2):
#   print(f"Nombre: {nombre.lower()}")
# elif (opcion == 3):
#   print(f"Nombre: {nombre.title()}")
# else:
#   "Por favor elija una opcion valida."

# -------------------------------------------------------------------

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# magnitud = int(input("Ingrese magnitud del terremoto: "))
# if(magnitud < 0):
#   print("Ingrese un numero positivo")
# elif (magnitud < 3):
#   print("Muy leve")
# elif (3 <= magnitud < 4):
#   print("Leve")
# elif (4 <= magnitud < 5):
#   print("Moderado")
# elif (5 <= magnitud < 6):
#   print("Fuerte")
# elif (6 <= magnitud < 7):
#   print("Muy Fuerte")
# else:
#   print("Extremo")

# -------------------------------------------------------------------
# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año.
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# emisferio = input("Ingrese en que emisferio se encuentra (N/S): ")
# mes = int(input("Ingrese mes actual (en numero, ejemplo: enero = 1): "))
# dia = int(input("Ingrese dìa: "))

# if (emisferio.upper() == "N"):
#   if (mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20):
#     print("Usted se encuentra en invierno")
#   elif (mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20):
#     print("Usted se encuentra en primavera")
#   elif (mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20):
#     print("Usted se encuentra en verano")
#   elif (mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20):
#     print("Usted se encuentra en otoño")
# elif (emisferio.upper() == "S"):
#   if (mes == 12 and dia >= 21 or mes == 1 or mes == 2 or mes == 3 and dia <= 20):
#     print("Usted se encuentra en verano")
#   elif (mes == 3 and dia >= 21 or mes == 4 or mes == 5 or mes == 6 and dia <= 20):
#     print("Usted se encuentra en otoño")
#   elif (mes == 6 and dia >= 21 or mes == 7 or mes == 8 or mes == 9 and dia <= 20):
#     print("Usted se encuentra en invierno")
#   elif (mes == 9 and dia >= 21 or mes == 10 or mes == 11 or mes == 12 and dia <= 20):
#     print("Usted se encuentra en primavera")
# else:
#   print("Por favor ingrese un emisferio valido.")
#   print("Las opciones validas son unicamente N o S")