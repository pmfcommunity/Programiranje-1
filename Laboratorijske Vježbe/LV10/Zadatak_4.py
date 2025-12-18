# Napisati funkciju koja cita matricu (listu listi) iz fajla. Parametar funkcije je priodno naziv fajla. Matrica se zapisuje u posebnom
# formatu. 
# Prvi red sadrzi zapisana dva broja odvojena razmakom: broj redova i potom broj kolona. Potom, svaki sljedeci red sadrzi po jedan red 
# matrice, pri čemu su brojevi razdvojeni razmakom. 

def ispis_matrice(fajl): 
    with open(fajl, "r") as f:
        matrica = []
        for linija in f: 
            linija = linija.strip()
            matrica.append(linija.split(" "))
        broj_redova = len(matrica)
        broj_kolona = len(matrica[0])
        print(broj_redova, broj_kolona)
        for i in range(broj_redova):
            for j in range(broj_kolona):
                print(matrica[i][j], end=" ")
            print()

fajl = "Zadatak_4.txt"
ispis_matrice(fajl)