# Napisati program koji ispisuje tablicu mnozenja na sljedeci nacin:
# https://pmfunsaba.sharepoint.com/sites/KN100SIT100-Programiranje12526/Zajednicki%20dokumenti/Vjezbe/Laboratorijske%20vje%C5%BEbe/KN/LV2%20-%20Stringovi,%20print,%20operacije/LV%202%20-%20Stringovi,%20print,%20operacije%20(1).pdf?CT=1761859690440&OR=ItemsView&wdOrigin=TEAMSFILE.FILEBROWSER.DOCUMENTLIBRARY

# NAPOMENA: Ovaj zadatak ce se uraditi preko petlje.

n = int(input())

i = 1
while i <= n:
    for j in range(1, n + 1):
        print(f"{j} * {i} = {j * i}  |", end="")
    i += 1
    print()