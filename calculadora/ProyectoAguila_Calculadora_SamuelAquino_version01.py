"""
Crear un programa donde pida 2 numeros enteros, que saque por consola la Suma, resta, multiplicacion
y el resto de la division 

"""

def calculador():
    try:

        valor1 =  input("Primer valor: ")
        valor2 = input("Segundo valor: ")
    except:
        if isinstance (valor1, float):
             print (f"El numero {valor1} No es un numero entero")
        else: 
            if isinstance(valor2, float):
                print (f"El numero {valor2} no es un numero entero")

    try:

        if isinstance(valor1, int) and isinstance(valor2, int):
            print ("Suma: {}".format(valor1 + valor2))
            print ("Resta: {}".format(valor1 - valor2))
            print ("Multiplicacion: {}".format(valor1 * valor2))
            print ("Division: {}".format(valor1 // valor2))
            print ("Resto de la division: {}".format(valor1 % valor2))
    except:
        print ("Error de ingreso")

calculador()