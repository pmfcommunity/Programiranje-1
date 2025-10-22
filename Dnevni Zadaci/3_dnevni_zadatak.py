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
print(f"Kolicnik: {broj1 / broj2}")

# Mogli smo ispis takodjer napisati kao, npr:
# print("Zbir : ", broj1 + broj2) itd, ali ovaj nacin je laksi i citljiviji.
# Ili napisati varijable za rezultat sume, razlike, proizvoda i kolicnika, pa njih ispisati. 