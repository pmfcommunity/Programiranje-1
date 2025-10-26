# Napisati program koji trazi da se sa tastature unesu dvije stranice trougla a i b, te ugao gamma izmedju njih. 
# Ugao unosimo u stepenima. Program racuna i ispisuje duzinu trece stranice trougla. Ukoliko unesemo stranice
# duzina 6 i 4, te ugao od 30 stepeni, rezultat treba da bude 3.22967.
# https://samarski.craft.me/2025P1AV2

from math import sqrt, cos, radians 

a = int(input("Unesite stranicu a: "))
b = int(input("Unesite stranicu b: "))
gamma = int(input("Unesite ugao gamma: "))

gamma = radians(gamma) # Pretvaramo stepene u radijane

c = sqrt(a**2 + b**2 - 2 * a * b * cos(gamma))

print(f"Trougao c iznosi: {c}")