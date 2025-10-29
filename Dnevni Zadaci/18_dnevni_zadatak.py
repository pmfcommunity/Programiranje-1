# Korisnik unosi prirodan broj n. U jednom potezu, od broja se oduzima njegova najveca cifra. U narednom potezu, 
# od rezultata se oduzima njegova najveca cifra itd. Program treba odrediti i ispisati koliko poteza je potrebno
# da bi se doslo do nule. Na primjer, za broj 24 potrebno je 5 poteza (24 -> 20 -> 18 -> 10 -> 9 -> 0)

n = int(input("Unesite broj n: "))

if n > 0:
    broj_poteza = 0
    while n > 0:
        kopija = n
        cifra_broja = []

        while kopija > 0:
            zadnji_broj = kopija % 10
            cifra_broja.append(zadnji_broj)
            kopija = kopija // 10
        maksimum = max(cifra_broja)
        n = n - maksimum
        broj_poteza += 1
        print(f"Maksimum broja: {maksimum}, broj nakon oduzimanja: {n}, broj poteza: {broj_poteza}")
    print(f"Broj poteza da se dodje to broja 0: {broj_poteza}")
else: print("Broj nije prirodan!")