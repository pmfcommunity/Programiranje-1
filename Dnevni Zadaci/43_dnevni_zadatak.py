# Napisati program koji od korisnika trazi unos broja n, te n prirodnih brojeva. Program pronalazi dominantni
# broj u nizu. Za neki broj kazemo da je dominantan ukoliko se pojavljuje bar n/2 puta u nizu.

n = int(input())
niz = []

for i in range(n):
    niz.append(int(input()))

dominantni = n // 2
jel_dominantan = False 

rjecnik = {}

for broj in niz: 
    rjecnik.update({broj:niz.count(broj)})
print(rjecnik)

broj = 0
for kljuc, vrijednost in rjecnik.items():
    if vrijednost >= dominantni:
        jel_dominantan = True 
        broj = kljuc
        break 

if jel_dominantan:
    print(f"{broj} je dominantan broj.")
else:
    print("Nema dominantnog broja u nizu.")