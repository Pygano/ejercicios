# python3
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Cesar_Lopez
# Created Date: 06/07/2022
# version ='1.0'

"""
Ejercicio:

Hacer un programa que solicite en pantalla 2 números enteros y que realice con ello las operaciones básicas:
    Suma
    Resta
    Multiplicación
    División
    Residuo de división

Muestre el resultado en pantalla.
"""
#Pedir al usuario dos números enteros
num_1 = int(input("Ingresar un número entero: "))
num_2 = int(input("Ingresar un número entero: "))


#Hacer las 5 operaciones 
print("La suma de",num_1,"+",num_2,"=", num_1 + num_2) #Imprime la suma
print("La resta de",num_1,"-",num_2,"=", num_1 - num_2) #Imprime la resta
print("La multiplicación de",num_1,"*",num_2,"=", num_1 * num_2) #Imprime la multiplicación
print("La división de",num_1,"/",num_2,"=", round(num_1 / num_2, 3)) #Imprime la división
print("El residuo de división de",num_1,"%",num_2,"=", num_1 % num_2) #Imprime la el residuo de la división

