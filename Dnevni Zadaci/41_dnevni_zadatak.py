# Napisati program koji od korisnika trazi unos prirodnih brojeva, sve dok ne unese dva puta uzastopno isti broj. Program ispisuje 
# najveci prost broj koji je unesen od strane korisnika. Ukoliko nije unesen nijedan prost broj, program ispisuje 0. Svi uneseni brojevi
# se uzimaju u razmatranje. 

from math import sqrt

prethodni_broj = -1 
lista_brojeva = []

while True: 
    n = int(input())
    if  prethodni_broj != 0: 
        if n == prethodni_broj:
            break
        else: 
            prethodni_broj = n 
            lista_brojeva.append(n)

lista_prostih_brojeva = []
for broj in lista_brojeva: 
    
    if broj <= 1:
        continue
    
    if broj == 2: 
        lista_prostih_brojeva.append(broj)
        continue 
    
    if broj % 2 == 0:
        continue
        
    limit = int(sqrt(broj)) + 1
    jel_prost = True 
    
    for i in range(3, limit, 2):
        if broj % i == 0: 
            jel_prost = False 
            break
            
    if jel_prost: 
        lista_prostih_brojeva.append(broj)
if lista_prostih_brojeva:
    print(max(lista_prostih_brojeva))
else:
    print(0)