# Napisati program koji od korisnika traži da unese red kvadratne matrice. 
# Korisnik zatim unosi matricu. Program ispisuje najveći element matrice.

n = int(input("Unos dimenzije matrice (nxn): "))

lista_matrice = []

for i in range(n):
    for j in range(n): 
        x = int(input())
        lista_matrice.append(x)

print(max(lista_matrice))