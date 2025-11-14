# Napisati program koji crta grafikon funkcije sin x. Od korisnika se ocekuje da unese pocetak a i kraj b intervala, kao i broj podjela
# n intervala (a, b). Za funkcije sin x znamo da uzima vrijednosti iz [-1, 1]. Pretpostavljamo da cemo upotrijebiti 21 kucicu za visinu
# grafika.

from math import sin 

a = int(input())
b = int(input())
n = int(input())

xs = []
x_step = (b - a) / (n - 1)

for i in range (n):
    xs.append(a + i * x_step)
    
ys = [sin(x) for x in xs]

kucica = 21 
y_step = 2 / (kucica - 1)

for linija in range(n):
    donja_granica = -1 + linija * y_step
    gonja_granica = donja_granica + y_step 
    
    red = ""
    for y in ys: 
        if donja_granica <= y < gonja_granica:
            red += "*"
        else: red += " "
    print(red)