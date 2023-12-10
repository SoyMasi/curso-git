from random import randint

lvlpk1 = randint(1,80)
vidapk1 = 2*lvlpk1
vidapk2 = 80

while vidapk1 > 0 and vidapk2 > 0 : 
    # empieza el combate

    #turno pk1
    print("Turno pokemon 1\n")
    ataque_pk1 = randint(1,2)
    if ataque_pk1 == 1:
        print("ataque achumaca")
        vidapk2 -= 10
    elif ataque_pk1 == 2:
        print("ataque superachumaca")
        vidapk2 -= 15

    print("La vida del pokemon enemigo es {}, la vida de mi pokemon es {}".format(vidapk1,vidapk2))
    #turno yo
    input("Enter para continuar ...")
    print("\nMi turno")
    ataque_pk2 = None
    while ataque_pk2 !="P" and ataque_pk2 != "A" and ataque_pk2 != "B":
        ataque_pk2 = input("¿Que ataque desesas realizar? [P] Placaje - [A] Pistola Agua - [B] Burbuja: ")

    if ataque_pk2 == "P":
        print("Ataque con placaje")
        vidapk1 -= 10
    elif ataque_pk2 == "A":
        print("Ataque con pistola agua")
        vidapk1 -= 12
    elif ataque_pk2 == "B":
        print("Ataque con burbuja")
        vidapk1 -= 9
    
    print("La vida del pokemon enemigo es {}\n la vida de mi pokemon es {}".format("#" * vidapk1, "#" * vidapk2))

if vidapk1 > vidapk2:
    print("El enemigo gana")
else: 
    print("Ganaste")