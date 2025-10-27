# Napisati program koji od korisnika traz unos sifre. Program treba da provjeri da li je unesena sifra sigurna i 
# ispise korisniku adekvatnu poruku. Sifra se smatra sigurnom ako zadovoljava sljedece: 
# • ima bar jedan broj [0-9]
# • ima bar jedan karakter iz skupa [!$#@]
# • duzina sifre je bar 6 karaktera 
# • duzina sifre je najvise 16 karaktera

sifra = input("Unesite vasu sifru: ")

if sifra == "": print("Niste unijeli sifru!")
else:
    ima_broj = False 
    ima_karakter = False 
    for c in sifra:
        if c.isdigit(): 
            ima_broj = True 
        if c == "!" or c == "$" or c == "#" or c == "@":
            ima_karakter = True 

    if ima_broj and ima_karakter and len(sifra) >= 6 and len(sifra) <= 16:
        print(f"Vasa sifra {sifra} je sigurna!")
    else: print(f"Vasa sifra {sifra} nije sigurna!")
     