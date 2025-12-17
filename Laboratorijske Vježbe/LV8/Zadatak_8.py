# Napisati program kojim se unosi matrica n x n elemenata. Program provjerava da li je matrica magicni kvadrat. 
# Magicni kvadrat je kvadrat kod kojeg su sume svih redova, kolona i glavne i suprotne dijagonale jednake. 

n = int(input())
matrica = []

for i in range(n):
    red = []
    for j in range(n): 
        red.append(int(input()))
    matrica.append(red)

ciljana_suma = sum(matrica[0])
jel_magicni = True 

for i in range(n):
    if sum(matrica[i]) != ciljana_suma: 
        jel_magicni = False 

for i in range(n):
    suma_trenutne_kolone = 0
    for j in range(n): 
        suma_trenutne_kolone += matrica[j][i]
    if suma_trenutne_kolone != ciljana_suma: 
        jel_magicni = False 
    
suma_glavne_dijagonale = 0 
suma_sporedne_dijagonale = 0 
for i in range(n):
        suma_glavne_dijagonale += matrica[i][i]
        suma_sporedne_dijagonale += matrica[i][n - 1 - i]

if suma_glavne_dijagonale != ciljana_suma or suma_sporedne_dijagonale != ciljana_suma: 
    jel_magicni = False 

if jel_magicni: 
    print("Broj je magicni")
else: print("Broj nije magicni")