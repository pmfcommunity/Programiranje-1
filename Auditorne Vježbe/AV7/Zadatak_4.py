# Napisati program koji od korisnika traži da unese red kvadratne matrice. 
# Korisnik zatim unosi matricu. Program nakon toga ispisuje red ili kolonu sa najvećom sumom.

n = int(input("Red kvadratne matrice: "))

lista_matrice = []
suma_reda = []
suma_kolone = [0] * n  

for i in range(n):
    red = []
    for j in range(n):
        x = int(input())
        red.append(x)
    lista_matrice.append(red)
        
for i in range(n):
    suma = 0
    for j in range(n):
        suma += lista_matrice[i][j]
        suma_kolone[j] += lista_matrice[i][j]
    suma_reda.append(suma)
    
najveci_red = max(suma_reda)
najveca_kolona = max(suma_kolone)

if najveci_red > najveca_kolona:
    print(najveci_red)
else: print(najveca_kolona)        