# Cifre 0, 4, 6, 8, i 9 su specificne po tome sto imaju rupaste dijelove u svom obliku. Broj 8 je poseban jer ima dvje rupe, dok ostali
# brojevi s rupama imaju samo jednu. 
# Program prima broj N i vraca zbir rupa za sve brojeve u opsegu od 1 do N (ukljucujuci i N)
# Na primjeru ispod (unos: 16), rezultat je 8 jer brojevi 4, 6, 8, 9, 10, 14, i 16 ukupno sadrze 8 rupa. 

n = int(input())
suma_rupa = 0

for i in range(1, n + 1):
    if i >= 10:
        kopija = i
        while kopija != 0: 
            cifra = kopija % 10 
            if cifra == 0 or cifra == 4 or cifra == 6 or cifra == 9: 
                suma_rupa += 1 
            if cifra == 8: 
                suma_rupa += 2
            kopija //= 10
    else: 
        if i == 0 or i == 4 or i == 6 or i == 9: 
            suma_rupa += 1 
        if i == 8: 
            suma_rupa += 2  
print(suma_rupa)    