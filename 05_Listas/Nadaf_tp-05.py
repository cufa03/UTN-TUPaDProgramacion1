## --- Resolucion Trabajo Practico Nº 5 - Lists --- ##
# ----------------------------------------------------------------------------------------

## 1) Crear una lista con las notas de 10 estudiantes.
## •Mostrar la lista completa.
## •Calcular y mostrar el promedio.
## •Indicar la nota más alta y la más baja.

# notas = [8.5, 7, 4.5, 9, 10, 8, 8.5, 5, 6, 7.5]
# suma = 0
# prom = 0
# alta = 0
# baja = 11
# for i in notas:
#   suma = suma + i
#   if i < baja:
#     baja = i
#   elif i > alta:
#     alta = i
    
# prom = suma / len(notas)

# print("La lista de notas es:", notas)
# print(f"El promedio de todas las notas es: {prom}")
# print(f"La nota mas baja es: {baja} y la mas alta es: {alta}")

# ----------------------------------------------------------------------------------------

## 2) Pedir al usuario que cargue 5 productos en una lista.
## • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
## • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

# productos = []

# for i in range(5):
#   producto = input("Ingrese un producto: ")
#   productos.append(producto)

# productosOrdenados = sorted(productos)
# print("La lista ordenada es:",productosOrdenados)

# opcion = input("Que producto desea eliminar?: ")
# if opcion in productosOrdenados:
#   productosOrdenados.remove(opcion)
#   print("La lista de productos actualizada es:",productosOrdenados)
# else:
#   print("El producto ingresado no existe")
# ----------------------------------------------------------------------------------------

## 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
## • Crear una lista con los pares y otra con los impares.
## • Mostrar cuántos números tiene cada lista.

# import random
# listaRandom = [random.randint(1, 100) for i in range(15)]
# listaPar = []
# listaImpar = []
# for i in listaRandom:
#   if i % 2 == 0:
#     listaPar.append(i)
#   else:
#     listaImpar.append(i)

# print(f"La lista par tiene {len(listaPar)} elementos y la lista impar tiene {len(listaImpar)} elementos")
# ----------------------------------------------------------------------------------------

## 4) Dada una lista con valores repetidos: datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
## • Crear una nueva lista sin elementos repetidos.
## • Mostrar el resultado.
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# nuevaLista = []
# for i in datos:
#   if i in nuevaLista:
#     pass
#   else:
#     nuevaLista.append(i)

# print("La lista sin repetidos es:", nuevaLista)

# ----------------------------------------------------------------------------------------

## 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
## • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
## • Mostrar la lista final actualizada.

# alumnos = ["Facundo", "Pablo", "Florencia", "Nicolas", "Agustina", "Fiorella", "Agustin", "Gabriela"]
# seguir = 1
# while seguir:
#   print("La lista de alumnos es:", alumnos)
#   print()
#   print("Desea agregar un nuevo estudiante o eliminar a un estudiante de la clase? ")
#   print()

#   pregunta = int(input("Opciones validas: 1 = Agregar o 2 = Eliminar: "))
#   print()

#   if pregunta == 1:
#     alumno = input("Ingrese el nombre del alumno a agregar: ")
#     alumnos.append(alumno)
#     print("Alumno agregado con exito")
#   elif pregunta == 2:
#     alumno = input("Ingrese el nombre del alumno a eliminar: ")
#     if alumno in alumnos:
#       alumnos.remove(alumno)
#       print(f"El alumno: {alumno} fue eliminado")
#     else:
#       print("El alumno ingresado no existe")
#   else:
#     print("Porfavor ingrese una opcion valida")
#   seguir = int(input("Desea seguir? 1 = si, 0 = no: "))

# print("La lista final es:", alumnos)

# ----------------------------------------------------------------------------------------

## 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

# numeros = [2,3,4,5,6,7,1]
# ultimo = numeros.pop()
# numeros.insert(0, ultimo)
# print("La nueva lista es:", numeros)

# ----------------------------------------------------------------------------------------

## 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
## • Calcular el promedio de las mínimas y el de las máximas.
## • Mostrar en qué día se registró la mayor amplitud térmica.

# clima = [[5,12],[7,12],[3,10],[8,11],[12,17],[16,23],[14,19]]
# minimaAcum = 0
# maximaAcum = 0
# minProm = 0
# maxProm = 0
# amplitudMax = 0
# diaAmplitud = 0
# for i in range(len(clima)):
#   minimaAcum = minimaAcum + clima[i][0]
#   maximaAcum = maximaAcum + clima[i][1]
#   if clima[i][1] - clima[i][0] > amplitudMax:
#     amplitudMax = clima[i][1] - clima[i][0]
#     diaAmplitud = i

# minProm = minimaAcum/7
# maxProm = maximaAcum/7

# if diaAmplitud == 0:
#   diaAmplitud = "Lunes"
# elif diaAmplitud == 1:
#   diaAmplitud = "Martes"
# elif diaAmplitud == 2:
#   diaAmplitud = "Miercoles"
# elif diaAmplitud == 3:
#   diaAmplitud = "Jueves"
# elif diaAmplitud == 4:
#   diaAmplitud = "Viernes"
# elif diaAmplitud == 5:
#   diaAmplitud = "Sabado"
# else:
#   diaAmplitud = "Domingo"

# print("El promedio de las temperaturas mínimas es:", minProm)
# print("El promedio de las temperaturas máximas es:", maxProm)
# print("El dia con mayor apmlitud fue:", diaAmplitud)
# ----------------------------------------------------------------------------------------

## 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
## • Mostrar el promedio de cada estudiante.
## • Mostrar el promedio de cada materia.

# matriz = [[7,7,9],[9,5,6],[9,9,9],[8,7,6],[8,10,9]]
# promedioEstudiante = [0,0,0,0,0]

# acumMateria1=0
# promMateria1=0

# acumMateria2=0
# promMateria2=0

# acumMateria3=0
# promMateria3=0
# for i in range(len(matriz)):
#   acumMateria1 = acumMateria1 + matriz[i][0]
#   acumMateria2 = acumMateria2 + matriz[i][1]
#   acumMateria3 = acumMateria3 + matriz[i][2]
#   promedioEstudiante[i] = (matriz[i][0] + matriz[i][1] + matriz[i][2]) / 3

# promMateria1 = acumMateria1 / 5
# promMateria2 = acumMateria2 / 5
# promMateria3 = acumMateria3 / 5

# print("El promedio de la materia 1 es:", promMateria1)
# print("El promedio de la materia 2 es:", promMateria2)
# print("El promedio de la materia 3 es:", promMateria3)
# print("El promedio de cada estudiante es:", promedioEstudiante)

# ----------------------------------------------------------------------------------------

## 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
## • Inicializarlo con guiones "-" representando casillas vacías.
## • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
## • Mostrar el tablero después de cada jugada.

# import random
# tablero = [ ["-","-","-"],
#             ["-","-","-"],
#             ["-","-","-"]]

# ganador = False
# turnos = 0
# jugadores = ["X", "O"]
# jugador = random.choice(jugadores)

# print(tablero)

# while not ganador and turnos < 9:
#   print("Turno del jugador:", jugador)
#   print("Valores posibles de fila y columna 0, 1, 2")
#   fila = int(input("Ingrese la fila donde quiere insertar su ficha: "))
#   col = int(input("Ingrese la columna donde quiere insertar su ficha: "))

#   while fila < 0 or fila > 2 or col < 0 or col > 2 or tablero[fila][col] != "-":
#     if tablero[fila][col] != "-":
#       print("Casilla ocupada, vuelva a intentar:")
#     else:
#       print("Posicion invalida, vuelva a intentar:")
#     print("Mostrando el tablero para que elija posicion:", tablero)
#     fila = int(input("Ingrese la fila donde quiere insertar su ficha: "))
#     col = int(input("Ingrese la columna donde quiere insertar su ficha: "))

#   if tablero[fila][col] == "-":
#     tablero[fila][col] = jugador
#     turnos = turnos + 1
#     for i in range(3):
#       if tablero[i][0] == tablero[i][1] == tablero[i][2] != "-":
#         ganador = True

#     for i in range(3):
#       if tablero[0][i] == tablero[1][i] == tablero[2][i] != "-":
#         ganador = True

#     if tablero[0][0] == tablero[1][1] == tablero[2][2] != "-":
#       ganador = True
#     if tablero[0][2] == tablero[1][1] == tablero[2][0] != "-":
#       ganador = True

#     if ganador:
#       print("El ganador es el jugador:", jugador)
#     else:
#       if jugador == "X":
#        jugador = "O"
#       else:
#        jugador = "X"
#     print(tablero)

# if not ganador:
#   print("Resulto en empate")

# ----------------------------------------------------------------------------------------

## 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
## 1) Mostrar el total vendido por cada producto.
## 2) Mostrar el día con mayores ventas totales.
## 3) Indicar cuál fue el producto más vendido en la semana.


## para resolver 1) al recorrer la matriz voy almacenando en totalProductos un acumulador por cada producto respetando los indices.
## para resolver 2) voy a acumular el valor de cada columna de la matriz en su respectiva posicion de la lista diaMasVentas[] y luego de ahi puedo obtener el dia con mayor ventas de la semana
## para resolver 3) para saber el producto mas vendido solo tengo que ver en la lista totalProductos nuevamente el elemento que mayor valor posea para luego mostrar el producto mas vendido en la semana

# import random

## creo la matriz 4 productos (filas) × 7 dias (columnas)
# matriz = [[random.randint(1, 100) for _ in range(7)] for _ in range(4)]
# dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

## 1) Total vendido por cada producto (suma por fila)
# totalProductos = [sum(fila) for fila in matriz]

## 2) Total por día (suma por columna)
# totalesPorDia = [sum(matriz[p][d] for p in range(4)) for d in range(7)]
# indiceDiaMax = totalesPorDia.index(max(totalesPorDia))

## 3) Producto más vendido en la semana
# indiceProdMax = totalProductos.index(max(totalProductos))


# print("Matriz (producto x día):")
# for i, fila in enumerate(matriz, start=1):
#     print(f"Producto {i}: {fila}")

## Otra forma de imprimir los resultados es:
## print("Total de ventas del producto 1:", totalProductos[0])
## print("Total de ventas del producto 2:", totalProductos[1])
## print("Total de ventas del producto 3:", totalProductos[2])
## print("Total de ventas del producto 4:", totalProductos[3])

# for producto, total in enumerate(totalProductos, start=1):
#     print(f"Total de ventas del producto {producto}: {total}")
# print(f"El dia que tuvo mayores ventas fue el {dias[indiceDiaMax]} con {totalesPorDia[indiceDiaMax]} unidades vendidas.")
# print(f"El producto mas vendido: Producto {indiceProdMax+1} con {totalProductos[indiceProdMax]} unidades.")







