# Data je funkcija:
#        { x^3 + x^2 + 1,   x > 10
# f(x) = { sin(x)cos(x),    x pripada [0, 10)
#        { e^x,             x < 0
# Napraviti program koji od korisnika ocekuje unos x, i na osnovu unesene vrijednosti racuna f(x).

from math import sin, cos, radians, e 

x = int(input("Unesite broj x: "))

funkcija = 0 

if x >= 0 and x < 10: 
    x = radians(x)
    funkcija = sin(x) * cos(x)
if x > 10: 
    funkcija = x ** 3 + x ** 2 + 1
if x < 10: 
    funkcija = e ** x 

print(f"Rezultat f(x) je: {funkcija}")