# Korisnik unosi brojeve jedan ispod drugog. Kraj unosa korisnik oznacava sa "*". Program ispisuje broj najblizi
# nuli. Na primjer, za unesene brojeve 3, 15, 13, 1 - program ispisuje "3". Za brojeve -6, 7, -2, 5, -1, program
# ispisuje "-1".

lista_pozitivnih_brojeva = []
lista_negativnih_brojeva = []

while True: 
    unos = input("Unesite broj. Prekid oznacite sa '*': ")
    if unos == "*": break 
    broj = int(unos)
    if broj >= 0: lista_pozitivnih_brojeva.append(broj)
    if broj < 0: lista_negativnih_brojeva.append(broj)

if not lista_negativnih_brojeva:
    najmanji_pozitivni_broj = min(lista_pozitivnih_brojeva)
    print(f"Broj najblizi nuli je: {najmanji_pozitivni_broj}")
elif not lista_pozitivnih_brojeva:
    najveci_negativni_broj = max(lista_negativnih_brojeva)
    print(f"Broj najblizi nuli je: {najveci_negativni_broj}")
else: 
    najveci_negativni_broj = max(lista_negativnih_brojeva)
    najmanji_pozitivni_broj = min(lista_pozitivnih_brojeva)
    najblizi_nuli = min(najveci_negativni_broj, najmanji_pozitivni_broj)

    print(f"Broj najblizi nuli je: {najblizi_nuli}")