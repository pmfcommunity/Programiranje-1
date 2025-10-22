# Kreirati digitron. Od korisnika se trazi da unese dva cijela broja. Nakon unosa, program ispisuje sumu, razliku,
# proizvod i kolicnik unesenih brojeva. Moguci izgled programa koji se izvrsava u konzoli naveden je u postavci 
# zadatka, ciji se link moze pristupiti ovdje:
# https://pmfunsaba.sharepoint.com/sites/KN100SIT100-Programiranje12526/Zajednicki%20dokumenti/Dnevni%20zadaci/Zadatak%206.pdf

# NAPOMENA: Ovo je isti zadatak kao zadatak 3. Objasnjenje zadatka mozete pogledati tamo. 

print("Unesite prvi cijeli broj:")
broj1 = int(input())

print("Unesite drugi cijeli broj:")
broj2 = int(input())

print('-'*30)

print(f"Zbir    : {broj1 + broj2}")
print(f"Razlika : {broj1 - broj2}")
print(f"Proizvod: {broj1 * broj2}")
print(f"Kolicnik: {int(broj1 / broj2)}") # Drugi nacin da osiguramo da je ispis kolicnika tipa int.