# Korisnik unosi prirodan broj n. Program ispisuje dužinu  najdužeg raspona u kojem su sve uzastopne cifre veće od 4. 
# Na primjer, za ulaz 928632978158, imamo četiri raspona sa ciframa većim od 4 i to 9,  86, 978, 58. Najduži je raspon 978, pa se 
# njegova dužina, odnosno broj 3 ispisuje.

n = int(input())
lista_n = list(str(n))
lista_uzastopnih_cifara = []
uzastopne_cifre = ""

for lista in lista_n:
    broj = int(lista)
    if broj > 4: 
        uzastopne_cifre += str(broj)
    else:
        if uzastopne_cifre != "":
            lista_uzastopnih_cifara.append(uzastopne_cifre)
        uzastopne_cifre= ""
if uzastopne_cifre != "":
    lista_uzastopnih_cifara.append(uzastopne_cifre)
if not lista_uzastopnih_cifara:
    najveci_raspon = 0
    print(najveci_raspon)
else:
    print(lista_uzastopnih_cifara)
    najveci_raspon = max(lista_uzastopnih_cifara)
    print(len(najveci_raspon))