# Napisati program koji od korisnika trazi unos broja n. Program ispisuje trougao sacinjen od slova.

n = int(input())
broj = 65

for i in range(1, n + 1): 
    for j in range(1, i):
        print(" ", end=" ")
    for j in range(1, n - i + 2):
        char = chr(broj)
        print(char, end=" ") 
    broj += 1
    print()
        