# Napisati program koji od korisnika trazi da unese podatke o tri stutenda (ime, prezime, prosjek ocjena, procentu
# -alan broj bodova na predmetu Programiranje I). Program treba da ispise te podatke u formatiranom obliku.
# https://samarski.craft.me/2025P1AV2

ime_1 = input("Unesite ime prvog studenta: ")
prezime_1 = input("Unesite prezime prvog studenta: ")
prosjek_1 = float(input("Unesite prosjek prvog studenta: "))
broj_bodova_1 = int(input("Unesite procentualan broj bodova prvog studenta za predmet Prograiranje 1: ")) 
print()

ime_2 = input("Unesite ime drugog studenta: ")
prezime_2 = input("Unesite prezime drugog studenta: ")
prosjek_2 = float(input("Unesite prosjek drugog studenta: "))
broj_bodova_2 = int(input("Unesite procentualan broj bodova drugog studenta za predmet Prograiranje 1: "))
print()

ime_3 = input("Unesite ime treceg studenta: ")
prezime_3 = input("Unesite prezime treceg studenta: ")
prosjek_3 = float(input("Unesite prosjek treceg studenta: "))
broj_bodova_3 = int(input("Unesite procentualan broj bodova treceg studenta za predmet Prograiranje 1: "))  
print()

print(f"{'Ime':<10}{'Prezime':<10}{'Prosjek':<10}{'Broj bodova u %':<10}")
print(f"{ime_1:<10}{prezime_1:<10}{prosjek_1:<10}{broj_bodova_1:<10}")
print(f"{ime_2:<10}{prezime_2:<10}{prosjek_2:<10}{broj_bodova_2:<10}")
print(f"{ime_3:<10}{prezime_3:<10}{prosjek_3:<10}{broj_bodova_3:<10}")