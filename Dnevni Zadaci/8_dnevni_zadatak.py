# Napisati program koji narednim redoslijedom od korisnika uzima cetiri realne vrijednosti: alfa, n, k i h. 
# Vrijednosti se unose jedna ispod druge. Program ispisuje rezultat narednog izraza navedenom u postavci zadatka:
# https://pmfunsaba.sharepoint.com/sites/KN100SIT100-Programiranje12526/Zajednicki%20dokumenti/Dnevni%20zadaci/Zadatak%208.pdf
# Ukoliko korisnik unese vrijednosti 80, 56.21, 23.6 i 2.4, program ispisuje 0.37899857290382083

from math import radians, sqrt, pow, sin, cos

print("Unos vrijednosti alfa:")
alfa = int(input())

print("Unos vrijednosti n:")
n = float(input())

print("Unos vrijednosti k:")
k = float(input())

print("Unos vrijednosti h:")
h = float(input())

alfa = radians(alfa)

rezultat = ((2 * pow(k, 2 / 3)) / (sin(alfa) * sqrt(h + n))) * cos(alfa)

print(f"Rezultat je broj: {rezultat}")

# Funkcije "sin" i "cos" ocekuju da broj bude izrazen u radijanima. Unos broja alfa je izrazen u stepenima. Tako
# da, moramo pretvoriti vrijednost u radijane. Postoje dva nacina: prvi je najlaksi i vrsi se preko funkcije 
# radians (tj. math.radians() ako ukljucimo cijelu biblioteku) u "math" biblioteci. Drugi jeste da sami pretvorimo
# broj u radijane, preko formule:
# radijani = stepeni * (pi / 180)
# samo trebamo ukljuciti "pi" kad ukljucujemo odredjene funkcije iz biblioteke "math", inace bi samo koristili 
# math.pi