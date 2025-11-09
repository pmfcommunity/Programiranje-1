# Korisnik unsi tri cijela broja x, y, i z, jedan ispod drugog. Ako su svi brojevi razlicite parnosti (jedan paran, dva neparna ili 
# obrnuto) program ispisuje "Razlicita parnost", a u suprotnom ispisuje "Ista parnost"

x = int(input())
y = int(input())
z = int(input()) 

broj_parnih = 0 
broj_neparnih = 0 

if x % 2 == 0: broj_parnih += 1 
else: broj_neparnih += 1
if y % 2 == 0: broj_parnih += 1 
else: broj_neparnih += 1
if z % 2 == 0: broj_parnih += 1 
else: broj_neparnih += 1

if broj_neparnih == 0 or broj_parnih == 0: 
    print("Ista parnost")
else: 
    print("Razlicita parnost")