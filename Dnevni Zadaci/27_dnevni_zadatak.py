# Napisai program koji za unesei broj n ispisuje prvih n Fibonacijevih brojeva. Kao sto je poznato, Fibonacijevi brojevi su brojevi zi niza
# 1, 1, 2, 3, 5, 8, 13, .... 
# Drugacije receno, Fibonacijev niz pocinje sa dvije jedinice, te se svaki naredni broj dobija kao zbir prethodna dva. 

n = int(input())

a = 0 
b = 1 
sljedeci = b 

i = 1
print(sljedeci, end=" ")
while i < n: 
    print(sljedeci, end=" ")
    a, b = b, sljedeci
    sljedeci = a + b
    i += 1
print()