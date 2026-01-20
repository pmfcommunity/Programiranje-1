# Napraviti funkciju koja biljezi odredjene elemente teksta: interpunkcijske znake, broj znakova za novi red, 
# veznike (i, pa, te, ni, niti, ili, samo, dakle, zato, stoga, a, ali...)

def ispis_elemenata(fajl):
    with open(fajl, "r") as f: 
        interpunkcijski_znakovi = 0
        novi_red = 0
        veznici = 0
        for unos in f: 
            podaci = unos.split()
            for podatak in podaci: 
                if "." in podatak or "," in podatak or "!" in podatak or "?" in podatak: 
                    interpunkcijski_znakovi += 1
                if podatak[-1] == "\n": 
                    novi_red += 1
                podatak = podatak.lower()
                if "i" in podatak or "pa" in podatak or "te" in podatak or "ni" in podatak or "niti" in podatak or "ili" in podatak or "ili" in podatak or "samo" in podatak or "dakle" in podatak or "zato" in podatak or "stoga" in podatak or "a" in podatak or "ali" in podatak:
                    veznici += 1
        rjecnik = {
            "Interpunkcijski znakovi":interpunkcijski_znakovi,
            "Znakovi za novi red":novi_red,
            "Veznici":veznici
        }
        for kljuc, vrijednoist in rjecnik.items():
            print(f"{kljuc} : {vrijednoist}")
ime_fajla = "tekst.txt"
ispis_elemenata(ime_fajla)