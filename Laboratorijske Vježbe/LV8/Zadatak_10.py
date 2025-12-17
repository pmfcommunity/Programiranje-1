# Napisati funkciju koja izracunava binomni koefcijent. 

from math import factorial

def binomni_koefcijent(n, k): 
    return (factorial(n)) // (factorial(k) * factorial(n - k))

a = int(input())
b = int(input())
print(binomni_koefcijent(a, b))