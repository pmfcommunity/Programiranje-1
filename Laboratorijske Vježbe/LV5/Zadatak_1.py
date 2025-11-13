# Napisati program koji za zadato uneseno m ispisuje tablicu vrijednosti faktorijela do bbroja m, kao i pribliznu vrijednost faktorijela
# preko tzv Stirlingove formule. 
# n! = sqrt(2 * pi * n) * (n / e)^n 

from math import sqrt, pi, e 

n = int(input())

for i in range(1, n + 1): 
    faktorijel = 1 
    for j in range(1, i + 1):
        faktorijel *= j 
    stirling = sqrt(2 * pi * i) * (i / e) ** i 
    print(f"{i:<5}{faktorijel:<5}{round(stirling, 5):<5}")