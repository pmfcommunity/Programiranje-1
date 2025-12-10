# Napisati funkciju koja prihvata prirodan broj n, te vra´ca zbir svih cifara koje se ne pojavljuju u broju n. Cifre unutar broja n 
# se ne ponavljaju. Dakle, ukoliko je broj n jednak 2385, programce ispisati zbir brojeva 1, 4, 6, 7, 9 i 0.
# Napisati kratki testni program gdje se od korisnika traži unos broja n, te se ispisuje dobijena vrijednost.

def zbir_cifara(a):
    cifre = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    cifre_broja = []
    while a != 0: 
        cifra = a % 10 
        cifre_broja.append(cifra)
        a //= 10 
    suma = 0
    for cifra in cifre: 
        if cifra not in cifre_broja: 
            suma += cifra 
    return suma

n = int(input())
print(zbir_cifara(n))