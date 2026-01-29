# Napisati program koji od korisnika trazi unos broja n i n cijelih brojeva koji se smjestaju u listu. Program
# sortira sve proste brojeve u listi. Slozeni brojevi i broj 1 ostaju na originalnim pozicijama. Ukoliko 
# korisnik unese [14, 5, 3, 45, 43, 9, 11] lista ce nakon sortiranja postati [14, 3, 5, 45, 11, 9, 43]
import math 
def jel_prost(cifra):
    if cifra <= 1: return False 
    if cifra == 2: return True 
    if cifra % 2 == 0: return False 
    limit = int(math.sqrt(cifra)) + 1
    for djeljitelj in range(3, limit, 1):
        if cifra % djeljitelj == 0:
            return False 
    return True

n = int(input())
niz = []

for _ in range(n):
    niz.append(int(input()))

pozicija_prostih = []
prosti_brojevi = []
brojac = 0

for broj in niz: 
    if jel_prost(broj):
        pozicija_prostih.append(brojac)
        prosti_brojevi.append(broj)
    brojac += 1
print(f"Originalna lista:\n{niz}")
prosti_brojevi.sort()

i = 0
for index in pozicija_prostih: 
    niz[index] = prosti_brojevi[i]
    i += 1

print(f"Sortirana lista:\n{niz}")