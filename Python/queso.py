print("Cuanto te gusta el Queso")

puntuacion = 0
conta = 0
contb = 0
contc = 0

print("Pregunta 1: Que haces cuando ves una tabla de quesos?")
print("A - Salgo corriendo")
print("B- Pruebo uno de los quesos o incluso varios")
print("C - No puedo evitar devorarla")
opc1 = input("Ingrese una opcion (A/B/C): ")
opc1.upper()

if opc1 == "C":
    conta += 15
elif opc1 == "B":
    contb += 10
elif opc1 == "A":
    contc += 5

print("Pregunta 2: Como te gusta la hamburguesa?")
print("A -Sin queso")
print("B - Con queso")
print("C - Pan y Queso")
opc2 = input("Ingrese una opcion (A/B/C): ")
opc2.upper()

if opc2 == "C":
    conta += 15
elif opc2 == "B":
    contb += 10
elif opc2 == "A":
    contc += 5

    
print("Pregunta 3: Sos intolerante a la lactosa?")
print("A - Si")
print("B - A veces")
print("C - No")
opc3 = input("Ingrese una opcion (A/B/C): ")
opc3.upper()


if opc3 == "C":
    conta += 15
elif opc3 == "B":
    contb += 10
elif opc3 == "A":
    contc += 5

contotal = conta + contb + contc
if contotal > 25: 
    print("Te gusta el queso")
elif contotal >15:
    print("Te gusta un poco el queso")
elif contotal < 15: 
    print("No te gusta el queso")