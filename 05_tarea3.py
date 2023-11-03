operacion = int(input("""
Bienvenido a mi calculadora
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
Seleccione una opción para ejecutar
"""))

while operacion < 5:
    numero_1 = int(input("Ingrese el primer número: "))
    numero_2 = int(input("Ingrese el segundo número: "))
    resultado = 0

    if operacion == 1:
        resultado = numero_1 + numero_2
    elif operacion == 2:
        resultado = numero_1 - numero_2
    elif operacion == 3:
        resultado = numero_1 * numero_2
    elif operacion == 4:
        if numero_2 == 0:
            resultado = numero_1 / numero_2
        else:
            print("Error: No se puede dividir por cero.")
    else:
        print("Opción no válida")

    print(f"El resultado de la operación es {resultado}")

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








