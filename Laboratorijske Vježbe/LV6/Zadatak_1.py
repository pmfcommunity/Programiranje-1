# Napisati program koji od korisnika trazi da unosi brojeve dok ne unese vrijednost 0. Program ispisuje brojeve u rastucem poretku.

lista_brojeva = []

while True: 
    broj = int(input())
    if broj == 0: 
        break 
    else: lista_brojeva.append(broj)

if lista_brojeva: 
    lista_brojeva.sort()
    ispis = ""
    for broj in lista_brojeva: 
        ispis += str(broj) + " "
    print(ispis)
else: print()