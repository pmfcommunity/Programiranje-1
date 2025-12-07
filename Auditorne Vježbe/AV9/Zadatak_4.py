# Napisati funkciju koja proslijedjeu listu stringova (imena studenata) prikazuje kao report (izvjestaj). Izvjestaj ima naslov, datum,
# ispred imena svakog studenta se nalazi redni broj, a nakon ispisane liste nalazi se footer - potpis strucne osobe (ili komisije)

def izvjestaj(studenti): 
    print("Izvjestaj studenata, 07.12.2025. godine:\n")
    redni_broj = 1
    for student in studenti: 
        print(f"{redni_broj}. {student}")
        redni_broj += 1
    print()
    print("Suljo Dobromanovic")

lista_studenata = []

while True: 
    unos = input("Unos studenata: ")
    if unos == "": break 
    else: lista_studenata.append(unos)
izvjestaj(lista_studenata)