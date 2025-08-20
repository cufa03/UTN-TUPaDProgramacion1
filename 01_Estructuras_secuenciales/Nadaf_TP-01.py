# 1)
print("Hola Mundo!")

# 2)
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3)
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# 4)
radio = float(input("Ingrese el radio del círculo: "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print(f"El área del círculo es {area} y el perímetro es {perimetro}.")

# 5)
segundos = float(input("Ingrese el tiempo en segundos: "))
horas = segundos / 3600
print(f"{segundos} equivale a {horas} horas")

# 6)
numero = int(input("Ingrese un numero: "))
i = 1
while (i <= 10):
    resultado = i * numero
    print(f"{numero} x {i} = {resultado}")
    i = i + 1

# 7)
num1 = int(input("Ingrese el primer número entero(distinto de 0): "))
num2 = int(input("Ingrese el segundo número entero(distinto de 0): "))
print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} / {num2} = {num1/num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} - {num2} = {num1-num2}")

# 8)
altura = float(input("Ingrese su altura (en metros y cm): "))
peso = float(input("Ingrese su peso: "))
print(f"Su IMC es: {peso / (altura ** 2)}")

# 9)
celsius = float(input("Ingrese la temperatura en celsius: "))
print(f"{celsius} °C equivale a {((9/5)*celsius ) + 32} °F")

# 10)
num1 = float(input("Ingrese el primer numero"))
num2 = float(input("Ingrese el segundo numero"))
num3 = float(input("Ingrese el tercer numero"))
print(f"El promedio de los numeros ingresados es: {(num1 + num2 + num3) / 3}")