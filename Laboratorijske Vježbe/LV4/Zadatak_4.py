# Treba napisati program gdje nakon unesenog prirodnog broja n crta kucu sa krovom.

n = int(input("Unesite prirodan broj n: "))

if n > 0:
    for i in range(n - 1):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            if k == 0 or k == 2 * i:
                print("*", end="")
            else: 
                print(" ", end="")
        print()
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else: 
                print(" ", end=" ")
        print()
else: print(f"Broj {n} nije prirodan!")