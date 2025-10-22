# Kreirajte program koji racuna i ispisuje vrijednost izraza naveden u PDF fajlu.
# U novom redu ispisite vrijednost izraza ukoliko je umjesto 2^10 vrijednost 1^10.
# TESTIRANJE: Za originalni izraz rezultat treba da bude 0.379564. Za drugi izraz A poprima vrijednost 0.38067.

A = 1 / (2 + (3 / 4 + (5 / 6 + (7 / 8 + (9 / 2**10)))))
print(f"Ispis za originalni izraz: {A}")

A = 1 / (2 + (3 / 4 + (5 / 6 + (7 / 8 + (9 / 1**10)))))
print(f"Ispis izraza sa izmjenjenom vrijednoscu: {A}")

# Ovdje samo treba da se pazimo zagrada, jer Python - i ostali programski jezici - prati redoslijed operacija.
# Npr za izraz 1 - 2 * 3, Python ce pomnoziti brojeve 2 i 3, pa onda oduzeti sa brojem jedan. Prema tome rezultat
# ce biti -5. Takodjer, potencije (2^10 i 1^10) pisemo kao "**" u Pythonu.