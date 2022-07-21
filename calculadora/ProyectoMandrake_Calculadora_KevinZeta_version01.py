"""Ejercicio #0001 - Ejercicio de generación de código - Aprendiendo creando apps
Hacer un programa que solicite en pantalla 2 números enteros y
que realice con ello las funciones básicas
 (Suma, resta, multiplicación, división, residuo de división),
  y que muestre el resultado en pantalla."""
num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero entero: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division =  num1 / num2
residuo = num1 % num2
print(f"La suma de {num1} y {num2} = {suma}")
print(f"La resta de {num1} y {num2} = {resta}")
print(f"La multiplicacion de {num1} y {num2} = {multiplicacion}")
print(f"La division de {num1} y {num2} = {division}")
print(f"El modulo de {num1} y {num2} = {residuo}")