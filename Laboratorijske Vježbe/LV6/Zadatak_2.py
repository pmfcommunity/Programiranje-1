# Napisati program koji trazi unos prirodnog broja n i cijelih brojeva a, b. Program pravi listu od n elemenata popunjen slucajno 
# generisanim cijelim brojevima u rasponu a do b. Na kraju se ispisuje lista, sa elementima razdvojenim zarezom. Napravite sljedece
# varijante: 
# - Brojevi u nizu se smiju ponavljati
# - Brojevi u nizu se ne smiju ponavljati 

import random

n = int(input())
a = int(input())
b = int(input())

lista_brojeva = []
for _ in range(n):
    lista_brojeva.append(random.randint(a, b))

for broj in lista_brojeva: 
    print(broj, end=" ")
print()

lista_unikatnih = []
while len(lista_unikatnih) < n:
    broj = random.randint(a, b)
    if broj not in lista_unikatnih:
        lista_unikatnih.append(broj)
for broj in lista_unikatnih: 
    print(broj, end=" ")
print()