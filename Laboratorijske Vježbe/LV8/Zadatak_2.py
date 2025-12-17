# Napisati funkciju duzina_hipotenuza koja racuna duzinu hipotenuze za proslijedjene duzine stranica a i b. 

from math import sqrt 

def duzina_hipotenuze(x, y):
    return sqrt(x ** 2 + y ** 2)

a = int(input())
b = int(input())
print(duzina_hipotenuze(a, b))