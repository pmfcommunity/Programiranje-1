import math 
x = int(input("Unesite cijeli broj x: "))

kvadrat = round(math.sqrt(x))
kub = round(pow(x, 1/3))

if x == pow(kvadrat, 2):
    print(f"{x} je kvadrat broja {kvadrat}")
elif x == pow(kub, 3):
    print(f"{x} je kub broja {kub}")
else: print(f"{x} nije ni savrsen kvadrat, niti savrsen kub bilo kojeg broja.")