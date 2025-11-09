# Prirodan broj n nazivamo savrsenim ako je njegov zbir cifara jednak njegovom proizvodu cifara. Napisati program
# koji od korisnika trazi unos prirodnog broja n, a onda ponovo ispisuje broj n ispod kojeg ispisuje poruku 
# 'da' ili 'ne', u zavisnosti od toga da li je broj savrsen ili ne. 

broj = int(input())

kopija = broj 

suma = 0
proizvod = 1 
while kopija != 0: 
    cifra = kopija % 10 
    suma += cifra
    proizvod *= cifra
    kopija //= 10 

if suma == proizvod: 
    print(broj)
    print("da")
else:
    print(broj)
    print("ne")