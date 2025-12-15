# Napisati funkciju koja iz fajla čita srednji kurs (novčane) valute čija se oznaka unosi sa tastature. Fajl je preuzet sa portala 
# Centralne banke Bosne i Hercegovine. 

def srednji_kurs(file, index, index_write):
    with open(file, "r") as f: 
        f.readline()
        brojac_reda = 0
        for linija in f:  
            brojac_reda += 1 
            linija = linija.strip()
            if linija and brojac_reda == index: 
                element = linija.split(",")
                
                if len(element) > index: 
                    srednji_kurs = element[index].strip()
                    print(f"{srednji_kurs}")
                    return
    f.close()

fajl = "Zadatak_2.csv"
INDEX_SREDNJEG_CLANA = 5
indeks_za_ispis = int(input())
srednji_kurs(fajl, INDEX_SREDNJEG_CLANA, indeks_za_ispis)
