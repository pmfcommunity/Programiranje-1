# Za broj 1 kazemo da je super broj. Ukoliko je neki broj x super, tada su i brojevi 2x i 3x super. Na primjer,
# kako je broj 1 super, tada su super broji 2 i 3. Kako su 2 i 3 super, tada su super i brojevi 4, 6, 9 itd. 
# Istovremeno, brojevi 10 i 7 nisu super.
# Napisati program koji od korisnika trazi unos prirodnog broja n. Program ispisuje da li je uneseni broj super.

n = int(input("Unesite prirodni broj n: "))

if n > 0:
    while n % 2 == 0:
        n = n // 2
    while n % 3 == 0:
        n = n // 3
    if n == 1: print("Uneseni broj je super.")
    else: print("Uneseni broj nije super.")
else: print("Uneseni broj nije prirodan!")