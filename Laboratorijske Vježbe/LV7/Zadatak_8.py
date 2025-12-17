# Izracunati e^x koristeci Taylorov razvoj u red. Kao ulazni podaci unose se x i broj clanova reda koje sabiramo. 

from math import factorial, e

x = int(input())
n = int(input())

suma = 0 
for i in range(n): 
    suma += x ** i / factorial(i)
    
print(suma)
print(e)