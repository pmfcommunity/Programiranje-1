# Izracunati e^x koristeci Taylorov razvoj u red i pobrojavanje liste (list comprehension)
from math import prod 

n = 1000

i = 1 
x = 1 

lista_brojeva = [1]
while i <= n: 
    faktorijel = [j for j in range(1, i + 1)]
    clan = (x ** i) / prod(faktorijel)
    lista_brojeva.append(clan)
    i += 1 

print(sum(lista_brojeva))