# Napisati program koji od korisnika trazi da unese dva cijela broja. Program treba da izracuna i ispise izraz:
# https://pmfunsaba.sharepoint.com/sites/KN100SIT100-Programiranje12526/Zajednicki%20dokumenti/Vjezbe/Laboratorijske%20vje%C5%BEbe/KN/LV2%20-%20Stringovi,%20print,%20operacije/LV%202%20-%20Stringovi,%20print,%20operacije%20(1).pdf?CT=1761859690440&OR=ItemsView&wdOrigin=TEAMSFILE.FILEBROWSER.DOCUMENTLIBRARY

a = int(input("Unesite broj a: "))
b = int(input("Unesite broj b: "))

rezultat = ((a % b)**abs(a)) / b ** 2

print(f"Rezultat izraza je: {rezultat}")