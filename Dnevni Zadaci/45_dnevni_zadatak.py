# Napisati program koji kreira matricu brojeva n x n. U matrici se pojavljuje svaki broj od 1 do n^2, pri cemu
# se svaki broj pojavljuje tacno jednom. Brojevi su u matrici rasoredjeni slucajno. Napisati kratki testni program
# koji od korisnika trazi unos broja n, te uredno ispisuje generisanu matricu.

import random
n = int(input())

niz_brojeva = []
for i in range(0, n ** 2 + 1):
    niz_brojeva.append(i)
print(niz_brojeva)

random.shuffle(niz_brojeva)

matrica = []
brojac = 0

for i in range(n):
    red = []
    for j in range(n):
        red.append(niz_brojeva[brojac])
        brojac += 1
    matrica.append(red)
   
for red in matrica:
    for element in red: 
        print(f"{element:3d}", end=" ") 
    print()                     