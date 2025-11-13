# Poznato je da vrijedi: 
# ln 2 = (-1)^n-1 * (1 / n)
# Izracunati ln2 tako što ćemo sabrati prvih n članova reda (n se unosi na pocetku rada programa). Ispisati tako dobijenu pribliznu 
# vrijednost od ln2, i potom razliku između te vrijednosti i vrijednosti dobijene putem matematičke biblioteke.

from math import log

n = int(input())

ln = 0
for i in range(1, n + 1):
    ln += (-1) ** (i - 1) * (1 / i)

print(ln)
print(log(2))
print(log(2) - ln)