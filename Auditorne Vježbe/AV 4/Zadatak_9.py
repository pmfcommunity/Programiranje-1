# Napisati program koji od korisnika trazi unos prirodnog broja n.
# Program ispisuje piramidu visine n sacinjenu od zvjezdica.

n = int(input("Unesite prirodan broj n: "))

if n > 0:
    for i in range(n, 1, -1):
        for razmak in range(0, n - i):
            print("  ", end="")
        for j in range(i, 2*i - 1):
            print("* ", end="")
        for j in range(1, i - 1):
            print("* ", end="")
        print() 
