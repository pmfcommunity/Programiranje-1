# Data je atrica dimenzija m x n, pri cemu su njeni elementi nule ili jedinice. Jedinicama su oznacene pozicije na ojima se nalazi serveri
# dok nule predstavljaju lokacije bez servera. Dva servera mogu medjusobno komunicirati ako se nalaze u istom redu ili istoj koloni.
# Potrebno je napisati program koji omogucava unos naziva fajla od strane korisnika. Progra treba procitati matricu iz datoteke, 
# te izracunati i ispisati broj servera koji mogu komunicirati s barem jednim drugim serverom. 

naziv_fajla = input()
matrica = []
with open(naziv_fajla) as f: 
    while True: 
        linija = f.readline()
        if linija == "": break 
        
        red = [int(s) for s in linija.split(" ")]
        matrica.append(red)

broj_servera = 0 

for i in range(len(matrica)):
    for j in range(len(matrica[0])):
        if matrica[i][j] == 1:
            povezan = False 
            for k in range(len(matrica)):
                if i != k: 
                    if matrica[k][j] == 1: 
                        povezan = True 
                        break 
            for k in range(len(matrica[0])):
                if j != k: 
                    if matrica[i][k] == 1: 
                        povezan = True 
                        break 
            if povezan: 
                broj_servera += 1 
print(broj_servera)