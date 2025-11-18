# Napisati program koji zahtijeva unos prirodnog broja n, i puni tablicu prvih n prirodnih brojeva, kvadrata i faktorijela. 
# Potom program ispisuje vrijednosti u tabelarnom obliku.

def faktorijel(m): 
    faktorijel = 1 
    for i in range(1, m + 1): 
        faktorijel *= i
    return faktorijel

n = int(input())

for i in range(1, n + 1): 
    print(f"{i:<3}{i ** 2:<3}{faktorijel(i):<3}")