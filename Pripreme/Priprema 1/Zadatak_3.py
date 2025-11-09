# Napisati program koji prima prirodan broj n i racuna sumu svih parova (i, j) gdje su i i j prirodni brojevi
# od 1 do n i gdje je proizvod i * j paran broj. program treba ispisati tu sumu.
# Na primjeru ispod, za n = 3 program ispisuje 20 jer sabira sve elemente parova: (1, 2), (2, 1), (2, 2), (2, 3)
# (3, 2)

n = int(input())
suma = 0 

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i * j) % 2 == 0: 
            suma += i + j 
print(suma)