# Napisati program kojim se unose dvije liste cijelih brojeva: unosi se prva lista, dok se ne unese 0, potom se unosi druga lista dok 
# se ne unese 0 , i potom se njihov presjek (elementi koji se nalaze u obje liste)

prva_lista = []
druga_lista = []

print("Unos prve liste:")
while True: 
    x = int(input())
    if x == 0: break 
    prva_lista.append(x)

print("Unos druge liste:")
while True: 
    x = int(input())
    if x == 0: break 
    druga_lista.append(x)

presjek = []
for prva in prva_lista:
        if prva in druga_lista: presjek.append(prva)

print(presjek)