# Za broj kazemo da je cudan ako je u potpunosti sastavljen od cifara 2 i 3. Korisnik unosi prirodan broj n. Program ispisuje n-ti cudan
# prirodan broj.

n = int(input())

if n > 0: 
    jel_cudan = True 
    while n != 0: 
        cifra = n % 10 
        if cifra != 3 and cifra != 2:
            jel_cudan = False
            break 
        n //= 10
    if jel_cudan: print("Broj je cudan.")
    else: print("Broj nije cudan.")
else: print("Greska! Broj nije prirodan!")