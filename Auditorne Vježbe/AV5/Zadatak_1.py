# Napisati program koji simulira bacanje novčića. Korisnik bira jedan od brojeva 0 (glava) ili 1 (pismo). 
# Program slučajno generiše jedan od  ishoda, te ukoliko je korisnik ispravno pogadao, program traži novi 
# unos. Ukoliko korisnik ne pogodi ishod bacanja, program prekida sa radom i ispisuje broj pogođenih bacanja.
# Dopuna: Moguće je najviše n bacanja (npr. n=10), i ako se dođe do broja bacanja koji je veći od n, program prekida sa radom.

import random 

n = 1 

while n != 11:
    novcic = int(input())
    novcic_random = random.randint(0, 1)
    if novcic == novcic_random:
        n += 1 
    else: break 
print(n)