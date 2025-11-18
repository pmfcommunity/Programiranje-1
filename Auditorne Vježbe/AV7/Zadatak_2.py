# Napisati program u kojem korisnik unosi cijele brojeve, sve dok ne unese nulu. Nakon unosa nule, program prvo ispisuje sve 
# negativne brojeve, a zatim sve pozitivne brojeve. Unutar svake grupe, brojevi trebaju biti u originalnom redoslijedu u kojem su 
# uneseni. Prilikom ispisa brojevi se ispisuju u istom redu, a odvojeni su jednim praznim mjestom.

lista_brojeva = []
lista_pozitivnih = []
lista_negativnih = []

while True: 
    x = int(input())
    if x == 0: break 
    if x > 0: lista_pozitivnih.append(x)
    if x < 0: lista_negativnih.append(x)
    lista_brojeva.append(x)
    
print("Originalna lista:")
[print(lista, end=" ") for lista in lista_brojeva]
print("")

if len(lista_negativnih) > 0:
    print("Negativni brojevi:")
    [print(negativni, end=" ") for negativni in lista_negativnih]
    print("")

if len(lista_pozitivnih) > 0:
    print("Pozitivni brojevi:")
    [print(pozitivni, end=" ") for pozitivni in lista_pozitivnih]
    print("")