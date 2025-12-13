# Napisati program koji unosi recenicu i potom je upisuje u fajl pod nazivom "recenica.txt"

recenica = input()
fajl = "Zadatak_1_b.txt"

with open(fajl, "x") as f: 
    f.write(recenica)
f.close()