# Napisati program koji za uneseni broj n ispisuje matricu dimenzija n x n. Matrica sadrzi brojeve od 1 do n^2. Svaki
# broj u matrici zauzima jednak broj mjesta. Koristi se jedan znak vise od roja znakova koje zauzive najveci broj u matrici.

n = int(input())

for i in range(1, n ** 2 + 1):
    print(f"{i:2}", end=" ")
    if i % n == 0:
        print("")