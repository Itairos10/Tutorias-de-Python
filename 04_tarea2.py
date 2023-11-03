operacion = int(input(""" Bienvenido a mi calculadora
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
Seleccione una opcion para ejecutar """))
while operacion < 5:
	error = False
	numero_1 = int(input("Ingrese el primer numero "))
	numero_2 = int(input("Ingrese el segundo numero "))
	resultado = 0
	if operacion == 1:
		resultado = numero_1 + numero_2
	elif operacion == 2:
		resultado = numero_1 - numero_2 
	elif operacion == 3:
		resultado = numero_1 * numero_2
	elif operacion == 4:
		if numero_2 == 0:
			error = True
			print("No se puede dividir entre 0")
		else:
			resultado = numero_1 / numero_2
	if not error:
		print(f" El resultado de la operacion es {resultado}")
	operacion = int(input("""
Bienvenido a mi calculadora
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
Seleccione una opción para ejecutar
"""))

print("Adiós!")

