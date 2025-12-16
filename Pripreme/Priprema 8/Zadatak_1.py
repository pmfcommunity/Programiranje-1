# Napisati program koji od korisnika zahtjeva unos 10 brojeva. Program ispisuje treci najveci broj.

lista_brojeva = []

for _ in range(10): 
    lista_brojeva.append(int(input()))
    
TRECI_NAJVECI = 3 

for broj in range(TRECI_NAJVECI): 
    maximum = max(lista_brojeva)
    lista_brojeva.remove(maximum)

print(max(lista_brojeva))