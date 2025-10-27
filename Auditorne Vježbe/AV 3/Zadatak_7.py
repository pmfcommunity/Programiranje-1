# Za trocifren prirodan broj kažemo da je dobar ako mu se neke  dvije cifre razlikuju za 1. 
# Napisati program koji od korisnika traži da unese trocifren broj, a zatim ispisuje da li je taj broj dobar.

trocifreni = int(input("Unesite trocifreni broj: "))
dobar = False 

if trocifreni >= 100 and trocifreni <= 999:
    stotica = trocifreni // 100
    desetica = (trocifreni // 10) % 10
    jedinica = trocifreni % 10
    if abs(stotica - desetica) == 1 or abs(stotica - jedinica) == 1 or abs(desetica - jedinica) == 1: dobar = True 
    if dobar: print(f"Broj {trocifreni} je dobar!")
    else: print(f"Broj {trocifreni} nije dobar!")
else: print(f"Broj {trocifreni} nije trocifreni!")    