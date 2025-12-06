# Za unesenu listu cijelih brojeva, napraviti i ispisati novu koja sadrži iste elemente kao polazna lista, 
# ali u kojoj su nule pomjerene na kraj. Na primjer, od [1, 0, 3, 2, 0, 5] dobijamo [1, 3, 2, 5, 0, 0].

lista_brojeva = [1, 0, 3, 2, 0, 5]
lista_brojevi = []
brojac_nula = 0
for brojevi in lista_brojeva:
    if brojevi == 0: brojac_nula += 1
    else: lista_brojevi.append(brojevi)

i = 0 
while i < brojac_nula: 
    lista_brojevi.append(0)
    i += 1
print(lista_brojevi)