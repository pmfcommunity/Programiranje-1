# Napisati program u kojem korisnik unosi listu prirodnih brojeva (u jednom redu, razdvojene jednim praznim mjestom), a zatim 
# unosi brojeve a i b
# Ukoliko se u listi broj a uvijek pojavljuje prije broja b, program ispisuje indeks prvog pojavljivanja a. U suprotnom (ukoliko se 
# bilo koje b pojavljuje prije bilo kojeg a), program ispisuje "b prije a", ali umjesto naziva varijabli ispisuje njihove vrijednosti
# Moze se pretpostaviti da se i a i b pojavljuju barem jedanput u unesenoj listi

unos_liste = input()
lista_stringova = unos_liste.split(" ")
lista_brojeva = []

for broj in lista_stringova: 
    lista_brojeva.append(int(broj))
    
a = int(input())
b = int(input())

pozicija_a = len(lista_brojeva) - list(reversed(lista_brojeva)).index(a) - 1 
pozicija_b = lista_brojeva.index(b)

if pozicija_b < pozicija_a: 
    print(f"{a} prije {b}")
else: 
    print(lista_brojeva.index(a))