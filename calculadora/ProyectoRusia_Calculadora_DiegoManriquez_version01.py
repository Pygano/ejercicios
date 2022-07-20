# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = int(input('Ingrese el primer valor entero: '))
b = int(input('Ingresee el segundo valor entero: '))

def suma(num1,num2):
    return num1 + num2

def resta(num1,num2):
    return num1 - num2

def multiplicacion(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 /num2

def residuo(num1,num2):
    return num1 % num2

print(f"El resultado de la suma es: {suma(a,b)}")
print(f"El resultado de la resta es: {resta(a,b)}")
print(f"El resultado de la multiplicacion es: {multiplicacion(a,b)}")
print(f"El resultado de la division es: {division(a,b)}")
print(f"El residuo de la division es: {residuo(a,b)}")