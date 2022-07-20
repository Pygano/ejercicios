# Ejercicio:
# Hacer un programa que solicite en pantalla 2 numeros enteros
# y que realice con ello las funciones basicas (Suma, resta,
# multiplicacion, division, residuo de division), y que muestre
# el resultado en pantalla.

def sumar(num1,num2):
    return num1+num2

def restar(num1,num2):
    return num1-num2

def multiplicar(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

def residuo_division(num1,num2):
    return num1%num2

print("Digite el primer valor")
numero1=int(input())
print("Digite el segundo valor")
numero2=int(input())

print(f'La suma de {numero1} y {numero2} es: {sumar(numero1,numero2)}')
print(f'La resta de {numero1} y {numero2} es: {restar(numero1,numero2)}')
print(f'La multiplicacion de {numero1} y {numero2} es: {multiplicar(numero1,numero2)}')
print(f'La division de {numero1} y {numero2} es: {division(numero1,numero2)}')
print(f'El residuo de la division (modulo) de {numero1} y {numero2} es: {residuo_division(numero1,numero2)}')