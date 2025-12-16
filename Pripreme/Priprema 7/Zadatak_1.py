# Program od korisnika prvo trazi broj n. Nakon toga korisnik unosi n cijelih brojeva
# koje program smijesta u listu. Nakon unosa ovih brojeva korisnik unosi jos i vrijednost m. Program
# treba ukloniti m najmanjih i najvecih vrijednosti iz liste. Preostale vrijednosti trebaju biti sortirane od 
# najmanje ka najvecoj i ispisane u istom redu razdvojene praznim mjestom. Primjer:
# 4
# 2
# 6
# 8
# 1
# Ispis: 4 6 

n = int(input())
lista_brojeva = []

for _ in range(n):
    lista_brojeva.append(int(input()))

m = int(input())

lista_min_max = []
kopija = lista_brojeva
for broj in range(m): 
    minimum = min(kopija)
    maximum = max(kopija)
    lista_min_max.append(minimum)
    lista_min_max.append(maximum)
    kopija.remove(minimum)
    kopija.remove(maximum)    

kopija.sort()

ispis = ""
for broj in kopija: 
    ispis += str(broj) + " "
print(ispis)