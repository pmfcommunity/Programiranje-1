# Napisati program koji od korisnika traži unos cijelog broja n. Program ispisuje da li je uneseni broj 
# paran ili neparan.
# https://samarski.craft.me/2025P1AV3

n = int(input("Unesite cijeli broj n: "))

if n % 2 == 0:
    print("Broj je paran")
else: print("Broj je ne paran")

# Provjeravamo da li je broj paran ako, tokom dijeljenja sa brojem 2, ne daje ostatak. 