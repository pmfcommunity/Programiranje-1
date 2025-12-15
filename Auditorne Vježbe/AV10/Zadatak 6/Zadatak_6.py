# Napisati program koji ucitava fajl "rezultati.txt". U tom fajlu se u svakoj liniji nalaze bodovi sa odredjenog dijela ispita za jednog 
# studenta, na primjer: 
# LV-Test-1 8.5
# I-parcijalna 15
# LV-Test-2 7
# Zavrsni ispit 35
# Program treba da sabere sa svih dijelova ispita i da na kraj fajla upise ukupan broj bodova studenta (prema gornjem primjeru):
# Ukupno 65.5 

fajl = "Zadatak_6.txt"
INDEX_OCJENA = 1 
suma = 0
with open(fajl, "r") as f:  
    for linija in f: 
        linija = linija.strip()
        if linija: 
            element = linija.split(" ")
            if len(element) >= INDEX_OCJENA: 
                ocjena = element[INDEX_OCJENA].strip()
                suma += float(ocjena)
with open(fajl, "a") as f: 
    f.write(f"\nUkupno {float(suma)}")