# Actividades:
# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos.
# Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt", "w") as archivo:
  archivo.write("Producto,Precio,Cantidad\n")
  archivo.write("Lapicera,120.5,30\n")
  archivo.write("Cuaderno,250.0,50\n")
  archivo.write("Mochila,1000.0,20\n")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r") as archivo:
  lineas = archivo.readlines()
  for linea in lineas[1:]:  # Hago esto para omitir porque la primera linea es el encabezado "Producto,Precio,Cantidad".
    nombre, precio, cantidad = linea.strip().split(",")
    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
   
# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.
print("\n----------------- Momento de agregar un nuevo producto -----------------\n")
nuevoProd_nombre = input("Ingrese el nombre del nuevo producto: ")
nuevoProd_precio = float(input("Ingrese el precio del nuevo producto: "))
nuevoProd_cantidad = int(input("Ingrese la cantidad del nuevo producto: "))
with open("productos.txt", "a") as archivo:
  archivo.write(f"{nuevoProd_nombre},{nuevoProd_precio},{nuevoProd_cantidad}\n")

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.
productos = []
with open("productos.txt", "r") as archivo:
  lineas = archivo.readlines()
  for linea in lineas[1:]:  # Hago esto para omitir porque la primera linea es el encabezado "Producto,Precio,Cantidad".
    nombre, precio, cantidad = linea.strip().split(",")
    producto = {
      "nombre": nombre,
      "precio": float(precio),
      "cantidad": int(cantidad)
    }
    print(producto)
    productos.append(producto)

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. 
# Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.
print("\n----------------- Momento de buscar un  producto -----------------\n")
producto_a_buscar = input("Ingrese el nombre del producto a buscar: ")
encontrado = False
for producto in productos:
  if producto["nombre"].lower() == producto_a_buscar.lower():
    print(f"Producto encontrado: Nombre: {producto["nombre"]}, Precio: ${producto["precio"]}, Cantidad: {producto["cantidad"]}")
    encontrado = True
    break
if not encontrado:
  print("Producto no encontrado.")
    
# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.
with open("productos.txt", "w") as archivo:
  archivo.write("Producto,Precio,Cantidad\n")
  for producto in productos:
    archivo.write(f"{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n")
