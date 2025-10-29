# Korisnik unosi prirodan broj n. Program ispisuje:
# 1. Supalj kvadrat stranice n sastavljen od zvjezdica. 
# 2. Suplju naopaku piramidu visine n sa okvirom od zvjezdica.
# 3. Baklavu visine 2 * n.

n = int(input("Unesite prirodan broj n: "))

if n > 0:
    print("Kvadrat")
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")
    
    print()
    print("Piramida:")
    for i in range(n, 0, -1): 
        for j in range(n - i):
            print(" ", end="")

        for k in range(2 * i - 1):
            if i == n or k == 0 or k == (2 * i - 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()
    
    print()
    print("Baklava:")
    for i in range(1, n): 
        for j in range(n - i):
            print(" ", end="")

        for k in range(2 * i - 1):
            if i == n or k == 0 or k == (2 * i - 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()
    for i in range(n - 1, 0, -1): 
        for j in range(n - i):
            print(" ", end="")

        for k in range(2 * i - 1):
            if i == n or k == 0 or k == (2 * i - 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()
else: print("Broj nije prirodan!")