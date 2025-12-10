# Napisati funkciju koja prihvata brojeve n i c. Funkcja raca ukupan broj pojavljivanja cifre c u svim brojevima od 1 do n. Broj n je 
# ukljucen u razmatranje.
# Napisati funkciju koja prihvata broj n, te cifru c. Funkcija ispisuje prvih n brojeva koji u sebi sadrze cifru c. Npr. za n = 6 i 
# c = 1, ispisuju se brojevi 1, 10, 11, 12, 13, 14.

def ukupan_broj_ponavljanja(n, c): 
    brojac = 0
    for i in range(1, n + 1):
        kopija = i
        if kopija < 10: 
            if c == kopija: brojac += 1
        if kopija >= 10: 
            while kopija != 0: 
                cifra = kopija % 10 
                if c == cifra: brojac += 1
                kopija //= 10        
    return brojac

def prvih_n_ponavljanja(n, c): 
    brojac = 0 
    i = 0
    lista_ponavljanja = []
    while True:
        if brojac == n: break  
        kopija = i 
        if kopija < 10: 
            if c == kopija: 
                brojac += 1
                lista_ponavljanja.append(c)
        if kopija >= 10:
            kopija_2 = kopija 
            nadjen = False
            while kopija != 0 and not nadjen: 
                cifra = kopija % 10 
                if c == cifra: 
                    lista_ponavljanja.append(kopija_2)
                    brojac += 1 
                    nadjen = True
                kopija //= 10
        i += 1
    for cifra in lista_ponavljanja:
        print(cifra, end=" ")
    print()
            

a = int(input())
b = int(input())

print(ukupan_broj_ponavljanja(a, b))
prvih_n_ponavljanja(a, b)