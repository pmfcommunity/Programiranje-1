# Napisati program koji otvara fajl pod nazivom "test01.in". U fajlu se nalaze temperature iz vise gradova, za svaki dan u sedmici. 
# Fajl je formatiran na sljedeci nacin. U prvo liiniji se nalazi veliko slovo P i ono oznacava ponedjeljak. U narednom redu se nalazi 
# naziv grada prazno mjesto pa izmjera temperatura za taj grad. U redi ispod je drugi grad sa svojom temperaturom. Linije sa gradovima 
# i temperaturama se ponavljaju dok se ne pojavi slovo U u zasebnom redu koje oznacava pocetak liste temperatura za utorak. Nakon slova 
# U opet slijedi lista istih gradova sa temperaturama za utorak. Ovaj uzorak se ponavlja za svih sedam dana u sedmici koji su oznaceni 
# slovima: P, U, S, C, P, S, N. Program ispisuje dva reda. U prvom se nalazi grad sa najnizom izmjerenom temperaturom, kao i nazivom 
# dana kada je izmjerena ta temperatura. U narednom se nalazi grad sa najvisom izmjerenom temperaturom i danom.

fajl = "Zadatak_3.txt"

mjerenja = []

dani = [ 
    "ponedjeljak", 
    "utorak",
    "srijeda",
    "cetvrtak",
    "petak",
    "subota",
    "nedjelja"
]
brojac_dana = -1

with open(fajl, "r") as f: 
    for linija in f: 
        linija = linija.strip()
        if len(linija) == 1 and linija.isalpha(): 
            brojac_dana += 1
            continue 
        
        dijelovi = linija.split()
        
        temperatura = float(dijelovi[-1])
        grad = " ".join(dijelovi[:-1])
        dan = dani[brojac_dana]
        
        mjerenja.append((grad, temperatura, dan))

min_mjerenje = min(mjerenja, key=lambda x: x[1])
max_mjerenje = max(mjerenja, key=lambda x: x[1])

print(f"{min_mjerenje[0]} {min_mjerenje[1]} {min_mjerenje[2]}")
print(f"{max_mjerenje[0]} {max_mjerenje[1]} {max_mjerenje[2]}")