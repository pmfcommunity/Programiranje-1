# Napisati funkciju koja ima dva parametra, prirodne brojeve m i n. Funkcija vraca NZD proslijedjenih brojeva. 

from math import gcd

def nzd(m, n):
    while m != n: 
        if m > n: 
            m -= n 
        else: 
            n -= m
    return m        

a = int(input())
b = int(input())
print(nzd(a, b))