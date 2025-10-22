# Napisite program koji trazi da se sa tastature unesu tri realna broja, a koji zatim ispisuje da li ta tri broja 
# mogu biti stranice pravouglog trougla. Pri unosu se ne zna koji je od tri unesena broja najveci (koji je 
# hipotenuza). Program treba da ponudi potvrdan odgovor za svaki od trojki (nije vazno da li je hipotenuza 
# unesena kao prvi ili drugi ili treci broj).
# Obavezno testirati program na ulaznim podacima 0.0003, 0.0004 i 0.0005. Poredak unosenja nije vazan. Zasto se 
# mogu jaiti problemi u ovom slucaju? Ukoliko i dalje sve bude radilo OK, dodate po jednu nulu. Pa opet...

from math import sqrt

print("Unesite realan broj a:")
a = float(input())

print("Unesite realan broj b:")
b = float(input())

print("Unesite realan broj c:")
c = float(input())

jelPravougli = (
    (a > b and a > c and a == sqrt(b**2 + c**2)) or \
    (b > a and b > c and b == sqrt(a**2 + c**2)) or \
    (c > a and c > b and c == sqrt(a**2 + b**2))
)

if jelPravougli:
    print(f"Brojevi {a}, {b}, {c} mogu biti stranice pravouglog trougla!")
else: print(f"Brojevi {a}, {b}, {c} ne mogu biti stranice pravouglog trougla!")
