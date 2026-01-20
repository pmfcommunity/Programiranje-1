# Napisati funkciju koja prima string kao parametar. Funkcija treba da izdvoji sve rijeci iz stringa 
# (rastavljene razmakom) i kreira rjecnik gdje su kljucevi rijeci, a vrijednosti su broj pojavljivanja
# te rijeci u stringu. 

def ponavljanje(string):
    lista = []
    string = string.split()
    for rijec in string: 
        if rijec[-1].lower() == "." or rijec[-1].lower() == ",":
            rijec = rijec[:-1]    
        if rijec.lower() not in lista:
            lista.append(rijec.lower())
    brojac = []
    for _ in range(len(lista)):
        brojac.append(0)
    for rijec in string: 
        if rijec[-1].lower() == "." or rijec[-1].lower() == ",":
            rijec = rijec[:-1]
        if rijec.lower() in lista:
            brojac[lista.index(rijec.lower())] += 1
    rjecnik = {}
    i = 0
    for rijec in lista: 
        rjecnik.update({rijec:brojac[i]})
        i += 1
    print(rjecnik)

recenica = "Ovo je primjer jedne recenice. Recenice su kul. Ovo je jos jedan primjer recenice."
ponavljanje(recenica)