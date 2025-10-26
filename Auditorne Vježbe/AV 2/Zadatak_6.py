# Napisati program koji od korisnika trazi da se unesu tri realna broja: a, b, i c, koja predstavljaju koefcijente
# kvadratne jednacine ax^2 + bx + c = 0, i potom ispisuje rjesenja kvadratne jednacine. 
# https://samarski.craft.me/2025P1AV2

from math import sqrt 

a = float(input("Unesite realan broj a: "))
b = float(input("Unesite realan broj b: "))
c = float(input("Unesite realan broj c: "))

D = b**2 - 4 * a * c 

if D >= 0: 
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(f"Rjesenja kvadratne jednacine su: {x1} i {x2}")
else: 
    print("Diskriminanta je negativna! Ne moze se izracunati rezultat.") 