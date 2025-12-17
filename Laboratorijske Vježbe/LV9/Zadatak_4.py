# Napisati funkciju koja vraca sve proste brojeve do n. 

from math import sqrt

def jel_prost(a):
    limit = int(sqrt(a)) + 1
    for i in range(3, limit, 2): 
        if a % i == 0: 
            return False 
    return True

n = int(input())

lista_prostih_brojeva = []
for i in range(n + 1): 
    if i <= 1:
        continue 
    if i == 2:
        lista_prostih_brojeva.append(i)
    if i % 2 == 0:
        continue
    if jel_prost(i):
        lista_prostih_brojeva.append(i)

print(lista_prostih_brojeva)