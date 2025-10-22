# Napisati program koji od korisnika trazi da unese prirodan broj 1 do 4.
# - Ukoliko korisnik unese broj 1, program od njega trazi unos jednog realnog broja. Program zatim ispisuje 
#   povrsinu i obim kruga sa unesenim poluprecnikom.
# - Ukoliko korisnik unese broj 2, program od njega trazi da unese dva prirodna broja a i b, te vraca vrijednost
#   povrsine i obima pravougaonika sa unesenim stranicama.
# - Ukoliko korisnik unese broj 3, program od njega trazi da unese realan broj a. Program zatim provjerava da li je
#   uneseni broj pozitivan, te ukoliko nije ispisuje odgovarajucu poruku. Inace program ispisuje povrsinu kvadrata
#   sa unesenom stranicom.
# - Ukoliko korisnik unese broj 4, program od njega trazi da unese dva cijela broja, te nakon toga program ispisuje
#   podatak o tome koji je broj veci (ili odgovarajucu poruku ukoliko su jednaki)/
# - Ukoliko korisnik ne unese nijedan od iznad navedenih brojeva, program ispisuje poruku: "Slusas li ti mene?"

from math import pi

print("Molim vas unesite neki broj od 1-4:")
broj = int(input())

if broj == 1: 
    print("Unesen je broj 1. Unesite sada jedan realan broj:")
    x = int(input())
    r = x 
    povrsina = r ** 2 * pi 
    obim = 2 * r * pi
    print(f"Povrsina kruga iznosi {povrsina}, a obim {obim}") 
elif broj == 2:
    print("Unesen je broj 2. Unesite prirodan broj a:")
    a = int(input())
    print("Unesite prirodan broj b:")
    b = int(input())
    
    if a < 1 and b < 1: print("Brojevi nisu prirodni!") # Najmanji prirodni broj je 1.
    else:
        povrsina = a * b 
        obim = 2 * (a + b)
        print(f"Povrsina pravougaonika iznosi {povrsina}, a obim {obim}")
elif broj == 3:
    print("Unesen je broj 3. Unesite sada jedan realan broj:")
    a = int(input())
    if a > 0:
        povrsina = a * 2
        print(f"Povrsina kvadrata iznosi {povrsina}")
    else: print(f"Uneseni broj {a} nije pozitivan!")
elif broj == 4:
    print("Unesen je broj 4. Unesite prvi cijeli broj:")
    a = int(input())
    print("Unesite drugi cijeli broj:")
    b = int(input())
    
    # Ne radimo provjeru za cijele brojeve, int() provjevara da li su uneseni brojevi cjelobrojni koefcijenti.
    
    if a > b: print(f"Broj {a} je veci od broja {b}")
    if a < b: print(f"Broj {b} je veci od broja {a}")
    if a == b: print(f"Brojevi su jednaki!") 
else: print("Slusas li ti mene?")