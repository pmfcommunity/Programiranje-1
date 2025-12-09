# Napisati program koji generiše dva slucajna prirodna broja a i b manja od 1000, te jednu od cetiri osnovne matematicke 
# operacije (sabiranje, oduzimanje, množenje i dijeljenje). Kreirati varijablu rezultat, te u nju smjestiti ispravan rezultat 
# primjene generisane operacije nad brojevima a i b. Obratiti paznju da rezultat uvijek treba biti cijeli broj.
# Uredno ispisati generisano pitanje i tacan rezultat.

import random 

a = random.randrange(1, 1000)
b = random.randrange(1, 1000)
znak = random.choice("+-*/")

if znak == "+":
    rezultat = a + b 
    print(f"{a} {znak} {b} = {rezultat}")
if znak == "-":
    rezultat = a - b 
    print(f"{a} {znak} {b} = {rezultat}")
if znak == "*":
    rezultat = a * b 
    print(f"{a} {znak} {b} = {rezultat}")
if znak == "/":
    rezultat = a / b 
    print(f"{a} {znak} {b} = {rezultat}")