print("Preparando una choco:")
print("Voy a la cocina")
print("Abro la heladera")

hay_leche = input("¿Hay Leche? (S/N): ")
hay_leche.upper()

if hay_leche == "S":
    print("Saco la leche de la heladera..")
elif hay_leche == "N":
    print("No tengo leche")
    print("Salgo a comprar leche")
else: 
    print("Opcion invalida")

hay_nesquik = input("¿Hay nesquik? (S/N): ")
hay_nesquik.upper()

if hay_nesquik == "S":
    print("Agarro nesquik")
    print("Caliento la leche")
    print("Mezclo la leche con el nesquik")
    print("disfruto")