# Napisati program koji od korisnika zahtijeva unos dvije rijeci. Program treba ispisati koliko 
# znakova se nalazi u prvoj ali ne i u drugoj rijeci. Program ne pravi razliku izmedju malih i velikih slova.

prva = input()
druga = input()

prva = prva.lower()
druga = druga.lower()

brojac = 0 

for znak in set(prva): 
    if znak not in druga: 
        brojac += 1 

print(brojac)