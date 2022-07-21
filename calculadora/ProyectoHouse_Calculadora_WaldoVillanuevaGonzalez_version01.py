# @utor:Wart
# Ejercicio 0001:
# Hacer un programa que solicite en pantalla 2 números enteros y que realice con ello las 
# funciones básicas (Suma, resta, multiplicación, división, residuo de división), y que muestre
# el resultado en pantalla.


print("Bienvenido a Calculator...")

var1 = int(input("Ingrese primer número: "))
var2 = int(input("Ingrese segundo número: "))

opciones = input("Ingrese la opcion deseada: \n\
    S s = Suma \n\
    R r = Resta \n\
    M m = Multiplicación \n\
    D d = División \n")

opcionesSelect = opciones.lower()

if opcionesSelect == "s":
    suma = f"EL resultado de la suma de {var1} mas {var2} es igual a: {var1 + var2}"
    print(suma)

elif opcionesSelect == "r":
    print(f"EL resultado de la resta de {var1} menos {var2} es igual a: {var1 - var2}")

elif opcionesSelect == "m":
    print(f"EL resultado de la multiplicación de {var1} por {var2} es igual a: {var1 * var2}")

elif opcionesSelect == "d":
    print(f"EL resultado de la división de {var1} entre {var2} es igual a: {var1 / var2}",f"y su residuo es: {var1 % var2}")

elif opcionesSelect != "s" or "r" or "m" or "d":
    print("Opcion ingresada no valida, intente nuevamente")
