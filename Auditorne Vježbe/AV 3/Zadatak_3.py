# Napisati program koji od korisnika traži unos tri cijela broja x, y i z. Program ispisuje da li su svi 
# uneseni brojevi različiti, da li postoje dva jednaka ili su svi jednaki? Ispisuje se prikladna poruka.

x = int(input("Unesite cijeli broj x: "))
y = int(input("Unesite cijeli broj y: "))
z = int(input("Unesite cijeli broj z: "))

if x == y and x == z and y == z:
    print(f"Brojevi {x}, {y}, i {z} su jednaki.")
if x == y and x != z and y != z:
    print(f"Brojevi {x} i {y} su jednaki.")
if x != y and x == z and y != z:
    print(f"Brojevi {x} i {z} su jednaki.")
if x != y and x != z and y == z:
    print(f"Brojevi {y} i {z} su jednaki.")
if x != y and x != z and y != z:
    print(f"Brojevi {x}, {y}, i {z} nisu jednaki.")