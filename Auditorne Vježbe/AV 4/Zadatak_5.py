# Napisati program koji od korisnika trazi unos cijelog broja n.
# Program ispisuje n slucajnih cijelih brojeva izmedju 10 i 100. 
# Brojevi su ispisani u jednom redu i razdvojeni su zarezom. 
# Nakon posljednjeg broja u nizu ne nalazi se zarez
import random 

n = int(input("Unesite cijeli broj n: "))

lista = []

for i in range(n):
    rand_broj = random.randrange(10, 100)
    lista.append(rand_broj)
print(", ".join(str(x) for x in lista))

# Fakticki "print(lista)" je tacno po tom uslovu u postavci, ali tako ispisuje i [] 