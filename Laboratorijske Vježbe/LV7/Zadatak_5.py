# Funckija math.prod kao parametar uzima listu, i vraca proizvod (produkt) svih elemenata liste. Razmisliti kako bi se 
# mogla napisati funkcija za izracun faktorijela na jednsotavan nacin. 

from math import prod 

def faktorijel(x): 
    lista_brojeva = [i for i in range(1, x + 1)]
    return prod(lista_brojeva)

n = int(input())
print(faktorijel(n))