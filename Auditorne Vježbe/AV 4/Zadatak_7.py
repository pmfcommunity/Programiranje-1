# Napisati program koji od korisnika trazi da unese prirodan broj n. 
# Program ispisuje okvir kvadrata dimenzija n x n sacinjen od zvjezdica. 
# Unutrasnjost nije ispunjena.

n = int(input("Unesite prirodan broj n: "))

if n > 0:
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")
else: print(f"Broj {n} nije prirodan broj!")            