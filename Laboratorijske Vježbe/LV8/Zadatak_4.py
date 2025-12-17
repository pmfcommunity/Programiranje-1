# Napisati program koji od korisnika trazi unos prirodnog broja n. Program treba da provjeri da li je uneseni broj palindrom. 

n = int(input())
broj_string = str(n)

if broj_string == broj_string[::-1]: 
    print(f"{n} je palindrom.")
else: 
    print(f"{n} nije palindrom")