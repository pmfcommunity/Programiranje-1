# Napisati funkciju koja prima rjecnik i pronalazi kljuc elementa sa najvecom vrijednostcu u rjecniku.

def najveca(rijecnik):
    lista_vrijednosi = []
    for kljuc, vrijednost in rijecnik.items():
        lista_vrijednosi.append(vrijednost)
    print(max(lista_vrijednosi))

rjecnik = {
    "Ana": 32,
    "Marko": 20,
    "Mihajl": 40
}
najveca(rjecnik)