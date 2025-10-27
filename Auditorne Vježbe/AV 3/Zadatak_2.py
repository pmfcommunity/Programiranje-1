# Napisati program koji od korisnika traži unos dva broja i potom ispisuje veći od njih. 
# Potom isto uraditi, ali ovaj put za stringove.
# https://samarski.craft.me/2025P1AV3
 
x = int(input("Unesite prvi broj x: "))
y = int(input("Unesite drugi broj y: "))

if x > y: 
    print(f"Broj {x} je veci od broja {y}")
else: print(f"Broj {y} je veci od broja {x}")

string_1 = input("Unesite prvi string: ")
string_2 = input("Unesite drugi string: ")

if string_1 > string_2:
    print(f"String {string_1} je veci od {string_2}")
else: print(f"String {string_2} je veci od {string_1}")

# Komparacija stringova je malo drugacija zato sto se porede prvo po velicini, a onda po ascii vrijednostima
# (Zato je string "pmf" veci od "PMF")