# Napisati program koji od korisnka trazi unos brojeva, sve dok ne unese 0. Nakon unosa broja 0, korisnik 
# unosi broj k. Program ispisuje k slucajno odabranih brojeva iz skupa unesenih. Program nikada ne bira dva 
# broja na istoj poziciji (npr. ne smijemo dva puta izabrati treci uneseni broj)

import random 

niz = []
while True: 
    unos = int(input())
    if unos == 0: break 
    else: niz.append(unos)

k = int(input())
if k > len(niz):
    print("Ne moze.")
else:
    niz_brojeva = []
    duzina_niza = len(niz)
    i = 1
    while i <= k:
        broj = random.randint(0, duzina_niza - 1)
        if niz[broj] not in niz_brojeva:
            niz_brojeva.append(niz[broj])
            i += 1
        else: continue 
    print(niz_brojeva)
