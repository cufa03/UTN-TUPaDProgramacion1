# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

# def factorial(n):
#   if n==1:
#     return 1
#   else:
#     return n * factorial(n-1)

# inputUsuario = int(input("Ingrese número: "))
# print(f"Ejecutando factorial de {inputUsuario}...")
# for i in range(1, inputUsuario + 1):
#   print(f"factorial de {i} = {factorial(i)}")

# ------------------------------------------------------------------------------

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# def fibonacci(num):
#   if num == 0 or num == 1:
#     return num
#   else:
#     return fibonacci(num - 1)+ fibonacci(num - 2)

# inputUsuario = int(input("Ingrese número: "))
# print(f"Ejecutando Fibonacci de {inputUsuario}...")
# for i in range(1, inputUsuario + 1):
#   print(f"Fibonacci de {i}: {fibonacci(i)}")

# ------------------------------------------------------------------------------

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

# def potencia(base,exp):
#   if exp == 0:
#     return 1
#   elif exp == 1:
#     return base
#   else:
#     return base * potencia(base, exp - 1)

# baseUsuario = int(input("Ingrese un numero entero para la BASE: "))
# expUsuario = int(input("Ingrese un numero entero para el EXPONENTE: "))
# print("Ejecutando calculo...")
# print(potencia(baseUsuario, expUsuario))

# ------------------------------------------------------------------------------

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
# Pasos para convertir un decimal a binario:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
# salida = [0,1,0,1]
# num = 0

# salida = []
# def convertir(num):
#   if num == 0:
#     return ""
#   else:
#     resto = num % 2
#     salida.append(resto)
#     convertir(num//2)

# inputUsuario = int(input("Ingrese un numero entero: "))
# print("Realizando calculo...")
# convertir(inputUsuario)
# inversa = ''.join(str(i) for i in reversed(salida))
# print(f"{inputUsuario} en base binaria es: {inversa}")

# ------------------------------------------------------------------------------

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

# def es_palindromo(palabra):
#   if len(palabra) <= 1:
#     return True
#   else:
#     if palabra[0] != palabra[-1]:
#       return False
#     else:
#       return es_palindromo(palabra[1:-1])
    
# inputUsuario = input("Ingrese una palabra: ").lower()

# if es_palindromo(inputUsuario):
#   print(f"La palabra '{inputUsuario}' es un palíndromo.")
# else:
#   print(f"La palabra '{inputUsuario}' no es un palíndromo.")

# ------------------------------------------------------------------------------

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

# def suma_digitos(n):
#   if n == 0:
#     return 0
#   else:
#     return n % 10 + suma_digitos(n // 10)
  
# inputUsuario = int(input("Ingrese un numero entero positivo: "))
# print(f"La suma de los digitos de {inputUsuario} es: {suma_digitos(inputUsuario)}")

# ------------------------------------------------------------------------------

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

# def contar_bloques(n):
#   if n == 1:
#     return 1
#   else:
#     return n + contar_bloques(n - 1)
  
# inputUsuario = int(input("Ingrese el número de bloques en el nivel más bajo: "))
# print(f"El total de bloques necesarios para construir la pirámide es: {contar_bloques(inputUsuario)}")

# ------------------------------------------------------------------------------

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

# def contar_digito(numero, digito):
#   if numero == 0:
#     return 0
#   else:
#     ultimo_digito = numero % 10
#     if ultimo_digito == digito:
#       return 1 + contar_digito(numero // 10, digito)
#     else:
#       return contar_digito(numero // 10, digito)
    
# numeroUsuario = int(input("Ingrese un número entero positivo: "))
# digitoUsuario = int(input("Ingrese un dígito (entre 0 y 9): "))
# print(f"El dígito ingresado aparece {contar_digito(numeroUsuario, digitoUsuario)}.")