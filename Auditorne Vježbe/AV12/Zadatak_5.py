# Napisati Python program koji ce procitat isve fajloe u tekucem folderu (direktoriju) koji imaju ekstenziju
# .txt i na osnovu njih ispisati koliko
# - Ima samoglasnika
# - Koliko ima suglasnika 
# - Koliko ima recenica 

import glob 

fajlovi = glob.glob("Zadatak_5/*.txt")
samoglasnici = ["a", "e", "i", "o", "u"]
broj_samoglasnika = 0
broj_suglasnika = 0 
broj_recenica = 0
for fajl in fajlovi:
    with open(fajl, "r") as f:
        for unos in f: 
            broj_recenica += unos.count(".") + unos.count("!") + unos.count("?")
            podaci = unos.split()
            for podatak in podaci: 
                for i in range(len(podatak)):   
                    if podatak[i].lower().isalpha():
                        if podatak[i].lower() in samoglasnici:
                            broj_samoglasnika += 1
                        else: broj_suglasnika += 1

rjecnik = {
    "Samoglasnici":broj_samoglasnika,
    "Suglasnici":broj_suglasnika,
    "Recenice":broj_recenica
}

print(rjecnik)