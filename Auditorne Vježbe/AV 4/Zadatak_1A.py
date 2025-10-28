# Napisati program koji od korisnika trazi unos brojeva a, b, i broj koraka n.
# Program ispisuje rijednosti x i funkcije sin(x) od tacke a do tacke b sa korakom (b - a) / n u tabeli. 

from math import sin

a = float(input("Unesite broj a: "))
b = float(input("Unesite broj b: "))
n = int(input("Unesite broj koraka: "))

korak = (b - a) / n 
x = a 
i = 0 

izraz_x = "x"
izraz_sin = "sin(x)"
print(f"{izraz_x:^10}|{izraz_sin:^10}")

while i <= 6:
    print(f"{x:10.6f}|{sin(x):10.6f}")
    x += korak
    i += 1