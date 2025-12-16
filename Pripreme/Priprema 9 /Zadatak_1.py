# Napisati program koji od korisnika zahtjeva unos neke recenice. Ukoliko se u recenici cesce
# pojavljuje slovo A od slova E program ispisuje A. Ukoliko se cesce pojavljuje slovo E od slova A
# program ispisuje E. Ukoliko se oba navedena slova pojavluju jednak broj pua program ispisuje AE. 
# Program ne treba praviti razliku izmedju velikih i malih slova (tj. broje se i velika i mala slova)

recenica = input()
recenica = recenica.upper()

brojac_A = 0
brojac_E = 0

for znak in recenica: 
    if znak == "A": brojac_A += 1
    if znak == "E": brojac_E += 1

if brojac_A > brojac_E: print("A")
if brojac_A < brojac_E: print("E")
if brojac_A == brojac_E: print("AE")