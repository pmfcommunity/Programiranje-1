# Napisati funkciju koja za date parametre (dva parametra, naziv ulaznog fajla i naziv izlaznog fajla) otvara ulazni fajl, cita sadrzaj
# i prepisuje ga u novi izlazni fajl. Izlazni fajl moze postojati, ali ne mora, u kojem slucaju se kreira. Prilikom prepisivanja, svi
# 13-cifreni brojevi (koji bi mogli predstavljati maticne brojeve, na primjer), zamjenjuje se sa 13 znakova x. 

def sakrij_broj(fajl, upis):
    with open(fajl, "r") as f:
        sadrzaj = []
        for linija in f: 
            linija = linija.strip()
            sadrzaj.append(linija.split(" "))
        for lista in sadrzaj: 
            maticni_broj = lista[2]
            if len(maticni_broj) == 13: 
                maticni_broj = len(maticni_broj) * "x"
                lista[2] = maticni_broj
        with open(upis, "x") as f: 
            for linija in sadrzaj: 
                f.write(" ".join(map(str, linija)) + "\n")

fajl1 = "Zadatak_3_ulaz.txt"
fajl2 = "Zadatak_3_izlaz.txt"
sakrij_broj(fajl1, fajl2)