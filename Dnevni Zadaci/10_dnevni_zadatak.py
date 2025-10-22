# Napisati program koji pretvara temperaturu iskazanu u stepenima Celzijusa u temperaturu iskazanu u stepenima 
# Farenheita. Odnos izmedju dvije temperature skale je u PDF postavke zadatka:
# https://pmfunsaba.sharepoint.com/sites/KN100SIT100-Programiranje12526/Zajednicki%20dokumenti/Dnevni%20zadaci/Zadatak%2010.pdf
# Za unos 29, program ispisuje 84.2.

print("Unesite vrijednost temperature u stepenima Celzijusa")
C = int(input())

F = C * (9 / 5) + 32

print(f"Iznos stepena Celzijusa u stepenima Farenheita je: {F}")