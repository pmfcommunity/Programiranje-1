# Napisati funkciju koja prihvata prirodni broj n, te vraca sa koliko nula zavrsava vrijednost faktorijela proslijedjenog broja. 
# Za osnovnu verziju programa, napisati program koji uspjesno radi sa manjim brojevima. 
# Npr. za n = 3, program ispisuje 0. Za n = 5, ispisuje se 1, dok se za broj 100 ispisuje 24. Za 1000, program ispisuje broj 249.

def broj_nula_faktorijela(n):
    faktorijel = 1 
    for i in range(1, n + 1): 
        faktorijel *= i 
    brojac_nula = 0 
    kopija = faktorijel
    while kopija != 0:
        cifra = kopija % 10 
        if cifra != 0: break 
        else: brojac_nula += 1
        kopija //= 10
    return brojac_nula

a = int(input())
print(broj_nula_faktorijela(a))