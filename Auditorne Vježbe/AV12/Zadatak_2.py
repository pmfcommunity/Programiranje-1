# Napisati program koji od korisnika trazi unos imena fajla, otvara fajl i broji samoglasnike. Na kraju, program
# ispisuje svaki samoglasnik i broj njegovih pojavljivanja (redoslijed je vazan - abecedno), pri cemu se ne 
# ispisuje samoglasnik koji se nije pojavio.

fajl = "samoglasnici.txt" # neda mi se preko inputa iskreno

with open(fajl, "r") as f:
    brojac_a = 0
    brojac_e = 0
    brojac_i = 0
    brojac_o = 0
    brojac_u = 0
    for unos in f: 
        podaci = unos.split()
        for podatak in podaci: 
            if podatak == "a":
                brojac_a += 1
            if podatak == "e":
                brojac_e += 1
            if podatak == "i":
                brojac_i += 1
            if podatak == "o":
                brojac_o += 1
            if podatak == "u":
                brojac_u += 1
    rijecnik = {
        "a": brojac_a,
        "e": brojac_e,
        "i": brojac_i,
        "o": brojac_o,
        "u": brojac_u
    }
    for kljuc, vrijednost in rijecnik.items():
        if vrijednost == 0:
            continue
        else:
            print(f"{kljuc} : {vrijednost}")