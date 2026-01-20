# Napraviti funkciju koja prima dva rjecnika ciji su elementi brojevi. Funkcija pravi novi rjecnik koji ima sve
# kljuceve iz prvog i drugog rjecnika, a vrijednosti za svaki kljuc su jednake zbiru ukoliko se kljuc nalazi 
# u oba rjecnika, u suprotnom, samo vrijednosti iz prvog (drugog) rjecnika. (Drugim rijecima, funkcija "sabira"
# vrijednosti koje se nalaze pod istim kljucem)

def dodaj_rjecnik(r1, r2):
    rezultat = {}
    for kljuc, vrijednost in r1.items():
        rezultat.update({kljuc:vrijednost})
    for kljuc, vrijednost in r2.items():
        if kljuc in rezultat:
            rezultat[kljuc] += vrijednost
        else:
            rezultat.update({kljuc:vrijednost})
    print(rezultat)

rjecnik1 = {
    "jabuka": 20,
    "kruska": 10
}

rjecnik2 = {
    "jabuka": 10,
    "jagoda": 40
}

dodaj_rjecnik(rjecnik1, rjecnik2)