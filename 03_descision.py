

print("Seleccione una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Residuo")

opcion = input("Escoga una opción (1/2/3/4): ")

if opcion in ('1', '2', '3', '4', '5'):
   
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        resultado = numero1 + numero2
        operacion = 'suma'
    elif opcion == '2':
        resultado = numero1 - numero2
        operacion = 'resta'
    elif opcion == '3':
        resultado = numero1 * numero2
        operacion = 'multiplicación'
    elif opcion == '5':
        resultado = numero1 % numero2
        operacion = 'residuo'   
    else:
        if numero2 == 0:
            print("Error: No es posible dividir entre cero.")
            resultado = None
        else:
            resultado = numero1 / numero2
            operacion = 'división'

    
    if resultado is not None:
        print(f"El resultado de la {operacion} es: {resultado}")
else:
    print("Opción no válida. Por favor, escoja una opción válida (1/2/3/4).")
mayor_o_menor_a_cero="Es mayor a cero" if resultado  > 0 else " Es un numero menor a cero"
print(mayor_o_menor_a_cero)

