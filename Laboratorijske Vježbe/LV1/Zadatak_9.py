# Napisati program koji trazi da korisnik unese dva realna broja a i b. Program racuna i ispisuje vrijednost 
# izraza: https://pmfunsaba.sharepoint.com/sites/KN100SIT100-Programiranje12526/Zajednicki%20dokumenti/Vjezbe/Laboratorijske%20vje%C5%BEbe/KN/LV1/LV%201%20-%20Unos,%20Ispis,%20Varijable.pdf?CT=1761856935255&OR=ItemsView&wdOrigin=TEAMSFILE.FILEBROWSER.DOCUMENTLIBRARY

a = float(input("Unesite broj a: "))
b = float(input("Unesite broj b: "))

rezultat = (a + b) / (1 + ((a**2 + b**2) / (a**2 - b**2)))

print(f"Rezultat izraza je: {rezultat}")

# "Sta se desava ukoliko korisnik unese dva jednaka broja?"
# -> Izbaci gresku jer se ne moze dijeliti sa 0. 
# "Sta se desava ako korisnik slucajno unese nesto sto nije broj?"
# -> Izbaci gresku da se treba unijeti realni broj.