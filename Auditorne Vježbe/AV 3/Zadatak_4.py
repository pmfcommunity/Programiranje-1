# Napisati program koji od korisnika traži unos tri (floating point) broja a, b i c. Program ispisuje da li 
# brojevi a, b i c predstavljaju dužine stranica pravouglog trougla. Poređenje vršiti sa 
# tačnošću ε=10^−6.

from math import sqrt

a = float(input("Unesite broj a: "))
b = float(input("Unesite broj b: "))
c = float(input("Unesite broj c: "))

if c == sqrt(a**2 + b**2):
    print(f"Brojevi {a}, {b}, i {c} predstavljaju duzine stranica pravouglog trougla.")
else: print(f"Brojevi {a}, {b}, i {c} ne predstavljaju duzine stranica pravouglog trougla.")