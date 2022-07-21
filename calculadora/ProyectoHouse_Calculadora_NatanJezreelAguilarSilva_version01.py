print("El siguiente programa es una herramienta para calcular sumas, restas, multiplicaciones y divisiones.")

x = float(input("Ingrese el primer valor:"))

y = float(input("Ingrese el segundo valor:"))

print("Ahora ingrese una de las siguientes operaciones:\n1)Suma\n2)Resta\n3)Multiplicacion\n4)Division")

op = input()

op = int(op)

if(op == 1):

                resp = x + y

                print("La operacion que ha escogido es suma la suma entre", x, " y ", y, " da como resultado:", resp)

elif(op == 2):

                resp = x - y

                print("La operacion que ha escogido es resta la resta entre", x, " y ", y, " da como resultado:", resp)

elif(op == 3):

                resp = x * y

                print("La operacion que ha escogido es multiplicacion la multiplicacion entre", x, " y ", y, " da como resultado:", resp)

elif(op == 4):

                resp = x / y

                rem = x % y

                print("La operacion que ha escogido es division la division entre", x, " y ", y, " da como resultado:", resp)

                print("\nSu remanente es:", rem)

else:

                print("La operacion seleccionada no existe")