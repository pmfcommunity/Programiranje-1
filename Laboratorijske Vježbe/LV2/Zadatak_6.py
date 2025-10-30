# Napisati program koji od korisnika trazi unos tri realna broja a, b, i c. Program ispisuje vrijednosti izraza
# https://pmfunsaba.sharepoint.com/sites/KN100SIT100-Programiranje12526/Zajednicki%20dokumenti/Vjezbe/Laboratorijske%20vje%C5%BEbe/KN/LV2%20-%20Stringovi,%20print,%20operacije/LV%202%20-%20Stringovi,%20print,%20operacije%20(1).pdf?CT=1761859690440&OR=ItemsView&wdOrigin=TEAMSFILE.FILEBROWSER.DOCUMENTLIBRARY
# zaokruzen na dvije decimale, bez koristenaj round funkcije. 

a = float(input("Unesite broj a: "))
b = float(input("Unesite broj b: "))
c = float(input("Unesite broj c: "))

rezultat = (abs(a + b - c) + abs(a - b + c) + abs(-a + b + c)) / 3

print(f"Rezultat izraza: {rezultat:.2f}")