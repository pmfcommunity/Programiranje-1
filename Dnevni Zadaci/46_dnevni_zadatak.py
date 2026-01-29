# Napisati funkciju koja prihvata listu cijelih brojeva izmedju 1 i n. Unutar liste, neki se brojevi pojavljuju
# jednom, neki se pojavljuju dva puta, dok se neki brojevi ne pojavljuju nikada. Pronaci sve brojeve izmedju 1 
# i n koji se ne pojavljuju u nizu. Vrijednost n predstavlja duzinu liste.

def ostali_brojevi(lista):
    velicina_niza = len(lista)
    niz_brojeva = [i for i in range(1, velicina_niza + 1)]
    drugi_brojevi = []
    
    for broj in niz_brojeva:
        if broj not in lista:
            drugi_brojevi.append(broj)
        else: continue
    if len(drugi_brojevi) > 0:
        print(f"Ostali brojevi koji se ne pojavljuju u nizu: {drugi_brojevi}")
    else:
        print("Nema brojeva koji ne dostaju u nizu.")
n = int(input())
niz = []

i = 0
while i < n: 
    unos = int(input())
    if unos > n or unos < 1: 
        print("Preveliki broj! Pokusajte ponovo.")
    else: 
        niz.append(unos)
        i += 1
ostali_brojevi(niz)