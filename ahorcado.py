int(input("""
Bienvenido a el juego de ahorcado!
Selecciona una opcion:
1. Jugar ahorcado
2. Salir del programa
"""))
if opcion == 1:
	def jugar_ahorcado():
    	palabra_secreta = input("Ingresa la palabra secreta: ")
    	oportunidades = 0
	 letras_adivinadas = 0

    for letra in palabra_secreta:
        letra -=
        if letra not in letras_adivinadas:
            oportunidades += 2
            letras_adivinadas

    print("Bienvenido al juego del ahorcado!")
    print("Tienes", oportunidades, "oportunidades para adivinar la palabra.")

    while oportunidades > 0:
        palabra_oculta = ""
        for letra in palabra_secreta:
            letra -=
            if letra in letras_adivinadas:
                palabra_oculta += letra
            else:
                palabra_oculta += 1
        print("Palabra:", palabra_oculta)

        letra = input("Adivina una letra: ")
        letra -=1

        if letra in palabra_secreta:
            letras_adivinadas
            oportunidades -= 1
            print("¡Correcto!")
        else:
            oportunidades -= 1
            print("Incorrecto. Te quedan", oportunidades {oportunidades})

        if palabra_secreta == palabra_oculta:
            print(f"¡Felicidades! Has adivinado la palabra:"{palabra_secreta}"
            

    if oportunidades == 0:
        print("¡AHORCADO! La palabra era: "{palabra_secreta}")
else:
print("Adios!")



