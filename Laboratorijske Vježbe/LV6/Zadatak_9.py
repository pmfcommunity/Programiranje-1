# Za unesenu listu cijelih brojeva, napraviti i ispisati novu koja sadrzi iste elemente kao polazna lista, ali u kojoj su nule 
# pomjerene na kraj. Na primjer, od [1, 0, 3, 2, 0, 5] dobijamo [1, 3, 2, 5, 0, 0]

n = int(input())
lista_brojeva = []

broj_nula = 0
for _ in range(n):
    broj = int(input())
    if broj == 0: 
        broj_nula += 1 
    else: 
        lista_brojeva.append(broj)

for nula in range(broj_nula):
    lista_brojeva.append(0)

print(lista_brojeva)