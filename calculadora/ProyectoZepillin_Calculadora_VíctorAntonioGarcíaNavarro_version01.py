print("---------- Calculadora ----------")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Residuo")
print("---------------------------------")
opcion = int(input("Selecciona una opción: "))
if(opcion>=1 and opcion<=5):
    num1 = int(input("Valor del número 1: "))
    num2 = int(input("Valor del número 2: "))
    resultado = 0
    if(opcion==1):
        resultado = num1 + num2
    elif(opcion==2):
        resultado = num1 - num2
    elif(opcion==3):
        resultado = num1 * num2
    elif(opcion==4):
        if(num2==0):
            print("La división por cero (0) no está definida")
        else:
            resultado = num1 / num2
    elif(opcion==5):
        if(num2==0):
            print("La división por cero (0) no está definida")
        else:
            resultado = num1 % num2
    print(f"El resultado es: {resultado}")
else:
    print("Opción no valida.")