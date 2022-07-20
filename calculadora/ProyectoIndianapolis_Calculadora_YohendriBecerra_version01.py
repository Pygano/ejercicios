var = int(input('Ingrese 1ra variable: '))
var2 = int(input('Ingrese 2da variable: '))


def suma():
	total = var + var2
	print('EL total de la suma es:', total)

def resta():
	total = var - var2
	print('EL total de la resta es:', total)

def multiplicacion():
	total = var * var2
	print('EL total de la multiplicacion es:', total)

def division():
	total = var / var2
	print('EL total de la division es:', total)

def divisionResto():
	total = var % var2
	print('EL resto de la division es:', total)


suma()
resta()
multiplicacion()
division()
divisionResto()