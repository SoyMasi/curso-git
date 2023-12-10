import random

hasTool = False
hasKey = 000

print('''Juego de la mazmorra \n
      --------------------------
      Eres el estudiante de un famoso alquimista, en uno de tus viajes para recolectar materiales para tu maestro caíste en una trampa.
      Esto hizo que cayeras en lo más profundo de una mazmorra, solo y desorientado busca la forma para salir!\n
      ''')

print('Frente a tí se encuentran dos caminos, uno tiene una tenue luz al fondo, el otro tiene pequeños charcos')
opcion = input('Que eliges?  OPCION (A) - Camino Luz tenue | OPCION (B) - Camino mojado: ')
opcion.upper()

if opcion == "A":
    print("\nCruzaste el camino con la luz tenue, pero te das cuenta de algo, el camino y la luz del tunel eran las fauces de un monstruo")
    input("*Moriste* ")
    
elif opcion == "B": 
    print("\nDecidiste cruzar el camino con charcos")
    print("Cada vez el agua sube más , hasta el punto de cubrirte las piernas por completo")
    print("Sientes algo debajo del agua, lo agarras?")
    opcion = input("Que eliges? OPCION (A) - Lo agarras | OPCION (B) - No lo agarras: ")
    if opcion == "A":
        print('\nFelicidades has conseguido la garra herramienta, algo extraña pero para algo servira..')
        hasTool = True
        print("\nSigues caminando y cada vez baja mas el agua hasta desaparecer")
        print("En una pared ves algo escrito, te detienes a observarlo?")
        opcion = input("OPCION (A) - SI | OPCION (B) - NO: ")
        if opcion == "A":
            print("\nConseguiste el codigo secreto!")
            hasKey = 123
            print("\nCaminando llegas a una puerta, al parecer tiene 3 orificios")
            print("Quizas aquí puede funcionar la garra, tienes la garra?")
            if hasTool == True:
                print("\nPerfecto, la puerta se ha abierto, puedes salir")
                print("Encuentras un pad numerico en el suelo quizas un codigo funcionaría")
                if hasKey != 000: 
                    print("\nPerfecto saliste de la mazmorra con una bolsa de oreos infinita!")
                    print("O al menos eso pensaste.. un lobo gigante se encuentra frente a tí  y te pregunta")
                    print("Oh humano, si quieres salir de la mazmorra debes adivinar el numero que en mi mente se encuentra, del 1 al 10, si te equivocas, me hare un festin con tus tripas")
                    numRandom = random.randint(1, 10)
                    opcion = int(input('Ingresa el numero : '))
                    if numRandom == opcion:
                        print("Lo has adivinado, eres libre de irte")
                        input("*Escapaste* ")
                    else: 
                        print("Ese no es el numero!")
                        input("*Moriste* ")
        elif opcion == "B":
            print("\nSolo quiero salir, no tengo tiempo para esto.")
            print("Caminando llegas a una puerta, al parecer tiene 3 orificios")
            print("Quizas aquí puede funcionar la garra, tienes la garra?")
            if hasTool == True:
                print("\nPerfecto, la puerta se ha abierto, puedes salir")
                print("Encuentras un pad numerico en el suelo quizas un codigo funcionaría")
                
            if hasKey == 000:
                print("No tienes el codigo para esto.")
    elif opcion == "B":
        print("\nSolo quiero salir, no tengo tiempo para esto")
        print("Sigues caminando y cada vez baja mas el agua hasta desaparecer")
        print("En una pared ves algo escrito, te detienes a observarlo?")
        opcion = input("OPCION (A) - SI | OPCION (B) - NO: ")
        if opcion == "A":
            print("\nConseguiste el codigo secreto!")
            hasKey = 123
            print("\nCaminando llegas a una puerta, al parecer tiene 3 orificios")
            print("No creo tener una herramienta para esto")
            print("Encuentras un pad numerico en el suelo quizas un codigo funcionaría")
            if hasKey != 000: 
                    print("\nConseguiste una bolsa de oreos infinita, estas encerrado de por vida pero tienes comida")
                    input("*Moriste de tanto comer oreos* ")
        elif opcion == "B":
            print("\nSolo quiero salir, no tengo tiempo para esto.")
            print("Caminando llegas a una puerta, al parecer tiene 3 orificios")
            print("No creo tener una herramienta para esto")
            print("Encuentras un pad numerico en el suelo quizas un codigo funcionaría")
            if hasKey == 000:
                print("\nNo tienes el codigo para esto.")
                print("Quedaste encerrado de por vida")
                input("*Moriste* ")