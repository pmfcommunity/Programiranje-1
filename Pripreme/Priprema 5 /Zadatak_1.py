# Korisnik unosi prirodne brojeve jedan ispod drugog. Kraj unosa oznacava praznim redo. Moze se pretpostaviti da su svi uneseni 
# brojevi razliciti. Napisati program koji pronalazi i ispisuje naveci proizvod bilo koja dva unesena broja. 

lista_brojeva = []

while True: 
    broj = input()
    if broj == "": break 
    else: lista_brojeva.append(int(broj))

prvi_max = max(lista_brojeva)

lista_bez_maxa = []
for broj in lista_brojeva:
    if broj == prvi_max: continue
    else: lista_bez_maxa.append(broj)

drugi_max = max(lista_bez_maxa)

print(prvi_max * drugi_max)