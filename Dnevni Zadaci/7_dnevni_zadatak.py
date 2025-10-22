# Neka je 'a' prvi uneseni broj, te neka je 'b' drugi uneseni broj u prethodnom zadatku. Nakon ispisa kolicnika, 
# izracunati i ispisati vrijednost izraza koje su navedene u postavci ovog zadatka:
# https://pmfunsaba.sharepoint.com/sites/KN100SIT100-Programiranje12526/Zajednicki%20dokumenti/Dnevni%20zadaci/Zadatak%207.pdf

# Pretpostavlja se da su vrijednosti iz zadatka 6 - 12 i 3.

# Ovdje cak i ne trebamo pitati korisnika da unese proizvoljne brojeve, posto je u postavci navedeno da su brojevi
# iz prethodnog zadatka, mozemo odmah staviti da je "a = 12" i "b = 3". Ali ovaj primjer koristi standardni unos
# brojeva preko inputa.

from math import sqrt, pow

print("Unesite prvi broj a:")
a = int(input())

print("Unesite drugi broj b:")
b = int(input())

print(f"Ispis kolicnika: {a / b}\n")

print(a ** 2) # ili a * a, ili cak pow(a, 2) - math.pow(a, 2)
print(a ** 10)
print(a ** 100)
print(a ** b)
print(sqrt(a))
print(pow(a, 1 / b))
print(pow(a, 11 / b))

# NAPOMENA 1: Ukljucujemo biblioteku "math" da bi mogli rijesiti zadatak. Bilo bi ispravno da napisemo samo 
# "import math", ali posto nam su u zadatku samo potrebne funkcije "sqrt" (koji prima samo jedan broj i racuna
# 2. korijen tog broja) i "pow" (koji prima dva broja - gdje je prvi baza, a druga potencija) mozemo reci programu
# da hocemo samo te dvije funkcije koristiti, pa mozemo napisati: 
# from math import sqrt, pow - doslovno kazemo "iz bilbioteke 'math' zelim samo importovati funkcije sqrt i pow",
# i ako koristimo ovaj nacin ukljucivanje biblioteke, ne moramo uvijek ukljucivati prefiks "math.", nego samo koristimo
# naziv funkcije. 
# NAPOMENA 1.5: Takodjer mozemo samo ukljuciti sqrt, zadnja dva izraza se mogu napisati koristeci oznaku "**", ali
# ovakav nacin racunanja (preko funkcije pow) pravi nas kod preglednijim, tj. citljivijim.

# NAPOMENA 2: "Trik" u rjesavanju zadnja dva izraza jeste da napisemo korijen kao potenciju. Gore smo naveli da 
# funkcija sqrt racuna 2. korijen nekog broja, to znaci da ne moze racunati treci, cetvrti, peti... n-ti korijen
# nekog broja. Stoga, koristeci se pravilima matematike pisemo izraz kao broj u korijenu (a) "na" potenciji broja 
# a (u prvom slucaju je broj '1', u drugom broj '11') koji se dijeli sa potencijom korijena (u oba slucaja je 
# potencija broj 'b').