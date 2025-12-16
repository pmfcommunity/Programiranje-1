# Program od korisnika zahtjevaunos naziva fajla. U fajlu se nalazi matrica sa brojevima. Program treba ispisati drugi red matrice. 
# Ukoliko matrica nemadva reda program ispisuje "Nema"

fajl = input()

with open(fajl, "r") as f: 
    prva_linija = f.readline()
    if prva_linija == "":
        print("Nema")
    else:
        druga_linija = f.readline()
        if druga_linija == "":
            print("Nema")
        else: 
            print(druga_linija)