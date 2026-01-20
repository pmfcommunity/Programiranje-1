# Napisati funkciju koja spaja dva rjecnika u jedan. Pri tome, ako se neki kljuc iz drugog rjecnika pojavljuje
# u prvom, krajnja vrijednost ce biti ona u drugom rjecniku. 

def spoji_rjecnik(rijecnik1, rijecnik2):
    novi_rjecnik = rijecnik1 | rijecnik2
    print(novi_rjecnik)

rjecnik1 = {
    "firma": "Toyota",
    "model": "Prius",
    "godina": 1994,
    "boja": "crna"
}

rjecnik2 = {
    "firma": "Ferrari",
    "boja": "crvena",
    "cijena": 500000
}

spoji_rjecnik(rjecnik1, rjecnik2)