# Napisati program koji cita "studenti.csv", koji sadrzi prezime i ime studenta i broj indeksa (dva polja), i na osnovu ovog fajla pravi
# novi fajl "izlaz.csv" koji ima iste kolone (prezime i ime, broj indeksa) uz dodatnu kolonu rednog broja na pocetku, ali su podaci slozeni
# po prezimenu i imenu. 

fajl = "Zadatak_2_ulaz.csv"
upis = "Zadatak_2_izlaz.csv"

with open(fajl, "r") as f: 
    sadrzaj = []
    f.readline()
    for linija in f: 
        linija = linija.strip()
        sadrzaj.append(linija.split(";"))
    sadrzaj.sort()
    redni_broj = 1
    for student in sadrzaj: 
        student.insert(0, redni_broj)
        redni_broj += 1   
    with open(upis, "a") as f: 
        f.write("Redni broj;Prezime i ime;Broj indeksa\n")
        for linija in sadrzaj: 
            upis_u_fajl = ";".join(map(str, linija))
            f.write(upis_u_fajl + "\n")