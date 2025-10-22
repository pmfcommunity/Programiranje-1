# Kreirati digitron koji poznaje cetiri osnovne operacije. Program simulira jednostavne operacije sa dva cijela
# broja. Nakon toga ispisuje sumu, razliku, proizvod i kolicnik neka dva broja. Moguci tekst koji se ispisuje u
# konzoli, i ostatak postavke je naveden u PDF zadatka:
# https://pmfunsaba.sharepoint.com/sites/KN100SIT100-Programiranje12526/Zajednicki%20dokumenti/Dnevni%20zadaci/Dnevni%20zadatak%203.pdf

print("Prvi cijeli broj sa kojim radimo je:")
broj1 = int(input()) # Inace bi unesena vrijednost bila tipa "string"

print("Drugi cijeli broj sa kojim radimo je:")
broj2 = int(input())

print('-'*30) 

print(f"Zbir    : {broj1 + broj2}")
print(f"Razlika : {broj1 - broj2}")
print(f"Proizvod: {broj1 * broj2}")
print(f"Kolicnik: {broj1 // broj2}")

# NAPOMENA ZA KOLICNIK: 
# Zapis kao "broj1 / broj2" je tacan, ali u postavci zadatka ispis kolicnika je cijeli broj.
# U Pythonu, ispis kolicnika je uvijek tipa float (decimalni brojevi), bez obzira jesu li uneseni brojevi tipa int
# (cijeli brojevi). Tako da ako je prvi uneseni broj '12' a drugi '2', ispis ce biti '4.0' umjesto samo '4'.
# Operacija '//' se koristi za cjelobrojno djeljenje i omogucava da se rezultat ispise kao cijeli broj. 

# Mogli smo ispis takodjer napisati kao, npr:
# print("Zbir : ", broj1 + broj2) itd, ali ovaj nacin je laksi i citljiviji.
# Ili napisati varijable za rezultat sume, razlike, proizvoda i kolicnika, pa njih ispisati. 