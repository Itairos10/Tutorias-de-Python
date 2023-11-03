again = True
while(again):
	option = int(input("""
Bienvenido al contador de letras, seleccione una opcion: 	
1. Contar letras
2. Salir del programa
Seleccione una opcion para continuar: """))
	if(option==1):
		palabra = input("Introduce una palabra: ")
		cantidad_letras = 0
		for letra in palabra:
    			cantidad_letras +=1	
		print(f"La palabra '{palabra}' tiene {cantidad_letras} letras.")

	else:
		again = False
print("Adios!")


    

