# U prethodni zadatak, dodati generisanje cetiri moguca odgovora. Tacno jedan odgovor treba biti tacan. Svi ostali odgovori 
# trebaju biti generisani slucajno. Pri tome, budite kreativni. Odgovori ne trebaju biti takvi da bude ocigledno koji je tacan rezultat.
# Ispisati kompletan tekst pitanja, te cetiri ponudena odgovora. Odgovori ne smiju biti uvijek u istom redoslijedu (npr. da je drugi 
# odgovor uvijek tacan ili da je uvijek najmanji odgovor tacan)

import random 

a = random.randrange(1, 1000)
b = random.randrange(1, 1000)
znak = random.choice("+-*/")

if znak == "+":
    rezultat = a + b 
if znak == "-":
    rezultat = a - b 
if znak == "*":
    rezultat = a * b 
if znak == "/":
    rezultat = a / b 
    
tacan_odgovor = rezultat 
pogresni_prvi = rezultat + random.randrange(1, 5)
pogresni_drugi = rezultat + random.randrange(1, 10)
pogresni_treci = rezultat - random.randrange(1, 15)

print(f"{a} {znak} {b} = ???") 

odgovori = [tacan_odgovor, pogresni_prvi, pogresni_drugi, pogresni_treci]

random.shuffle(odgovori)

brojac = 1
for odgovor in odgovori: 
    print(f"{brojac}. {odgovor}")
    brojac += 1 
pokusaj = float(input())
if pokusaj == tacan_odgovor: tacan_pokusaj = True 
else: tacan_pokusaj = False

if tacan_pokusaj: print("Odgovor je tacan.")
else: print(f"Netacno. Tacan odgovor je {tacan_odgovor}")
