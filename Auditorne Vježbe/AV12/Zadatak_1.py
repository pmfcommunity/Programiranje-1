# A) Napisati program koji prvo zahtijeva unos ključeva odvojenih razmakom, a potom unos vrijednosti (tako da se unose redom kako su 
# navedeni ključevi), također odvojenih razmakom. Program pravi novi rječnik, sa unesenim ključevima i vrijednostima.
# B) Provjeriti da li postoji stavka sa ključem aaa , pa ako postoji, ispisati Postoji  i nakon toga vrijednost za dati ključ, u 
# suprotnom Ne postoji .
# C) Potom ispisati novi rječnik, koristeći se običnom for petljom kroz rječnik.
# D) Poslije toga ispisati one stavke rječnika (ključ, vrijednost) za koje ključ počinje slovom k . 
# Koristiti svojstvo .items() .
# E) Obrisati stavku rječnika sa ključem bbb ukoliko postoji.
# F) Napraviti novi rječnik na osnovu prethodnog, koji sadrži samo one vrijednosti (stringove) koji su po dužini veći od ili 
# jednaki tri znaka.

unos_kljuceva = input()
unos_kljuceva = unos_kljuceva.split()

unos_vrijednosti = input()
unos_vrijednosti = unos_vrijednosti.split()

if len(unos_vrijednosti) != len(unos_kljuceva):
    print("Nisu iste duzine!")
else:
    dictionary = {}
    for i in range(len(unos_kljuceva)):
        dictionary.update({unos_kljuceva[i]:unos_vrijednosti[i]})
    if "aaa" in dictionary:
        print("Postoji")
        print(dictionary.get("aaa"))
    else: print("Ne postoji")
    for unos in dictionary:
        print(f"{unos} : {dictionary[unos]}")
    print()
    for kljuc, vrijednost in dictionary.items():
        if kljuc[0] == "k":
            print(f"{kljuc} : {vrijednost}") 
    novi_rjecnik = {}
    for kljuc, vrijednost in dictionary.items():
        if "bbb" in kljuc:
            continue 
        else: 
            novi_rjecnik.update({kljuc:vrijednost})
    print(novi_rjecnik)
    rjecnik = {}
    for kljuc, vrijednost in novi_rjecnik.items():
        if len(vrijednost) >= 3:
            rjecnik.update({kljuc:vrijednost})
    print(rjecnik)