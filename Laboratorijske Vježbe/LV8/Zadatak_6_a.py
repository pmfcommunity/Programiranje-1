# Napisati program koji za unesenu listu brojeva pravi sve kombinacije date liste od dva elementa. Napomena: Kominacija elemenata liste 
# [1, 2, 3, 4, 5] su 1, 2, zatim 1, 3 pa 1, 4, 1, 5, 2, 3, 2, 4 itd. Do 4, 5.

unos = input()
unos = unos.split(" ")

lista_brojeva = []
for broj in unos: 
    lista_brojeva.append(int(broj))

n = len(lista_brojeva)

for i in range(n):
    for j in range(i + 1, n): 
        print(f"{lista_brojeva[i]} {lista_brojeva[j]}")