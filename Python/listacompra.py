# Progama lista de la compra
# Que desea comprar? [Q] Para salir 
# > leche , Seguro que quiere añadir "leche"?
# [S / N ] > S . Leche añadido

lista = []

while True:
    input_user = input("¿Que desea comprar? [Q] para salir: ")
    if input_user == "Q":
        break
    elif input_user  in lista:
        print('{} ya está en la lista'.format(input_user))
    else:
        if input("¿Seguro que quiere añadir {} a la lista de la compra? [S/N] ".format(input_user)) == "S":
            lista.append(input_user)

print("La lista de la compra es: ")
print(lista)