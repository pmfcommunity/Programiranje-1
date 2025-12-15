# Napisati program koji učitava fajl "rijeci.txt" i broji koliko riječi ima u tom fajlu, pri čemu riječi mogu biti odvojene samo 
# razmakom ili zarezom i razmakom.

import re 

fajl = "Zadatak_5.txt"
with open(fajl, "r") as f: 
    sadrzaj = f.read()
    tekst = " ".join(sadrzaj.split())
    print(tekst)
    rezultat = re.split("[,\s]+", tekst)
    print(len(rezultat))