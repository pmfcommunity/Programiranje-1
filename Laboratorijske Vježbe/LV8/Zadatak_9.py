# Napisati program koji unosi listu rijeci u jednom redu (razdvojene razmakom) i u novom redu string kraj. Program zatim ispisuje 
# broj rijeci iz liste koje zavrsavaju sa kraj 
# Potom prepraviti program i napsiati funkciju roj_rijeci koja prihvata listu rijeci i string parametar kraj, koja vraca broj 
# rijeci iz liste koje zavrsavaju sa stringom kako je navedeno u parametru kraj. 

def broj_rijeci(lista, kraj): 
    brojac = 0
    for rijec in lista: 
        duzina = len(rijec) - len(kraj)
        if rijec[duzina:] == kraj: 
            brojac += 1 
    return brojac
    

unos = input()
unos_kraj = input()

unos = unos.split(" ")
print(broj_rijeci(unos, unos_kraj))