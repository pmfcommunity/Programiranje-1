# Napisati funkciju koja prihvata prirodan broj n, te vraca zbir svih cifara koje se ne pojavljuju u broju n. Cifre unutuar broja n se 
# mogu ponavjati. Dakle, ukoliko je broj n jednak 23285, program ce ispisati zbir brojeva 1, 4, 6, 7, 9 i 0. Napisati krati testni 
# program gdje se od korisnika trazi unos broja n, te se ispisuje dobijena vrijednost. 

def zbir_ne_pojavljujucih(n):
    cifre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cifre_unesenog = []
    kopija = n 
    while kopija != 0: 
        broj = kopija % 10 
        cifre_unesenog.append(broj)
        kopija //= 10
    suma = 0 
    for cifra in cifre: 
        if cifra not in cifre_unesenog:
            suma += cifra 
    return suma 

a = int(input())
print(zbir_ne_pojavljujucih(a))