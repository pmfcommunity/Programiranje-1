# Napisati program koji od korisnika trazi unos dva realna broja a i b, a zatim racuna sljedece matematicke 
# operacije i ispisuje ih korisniku:
# https://samarski.craft.me/2025P1AV2

a = float(input("Unesite realni broj a: "))
b = float(input("Unesite realni broj b: "))

print()
print(f"a + b = {a + b}")
print(f"a * b = {a * b}")
print(f"a / b = {round(a / b, 2)}")
print(f"a % b = {a % b}")
print(f"a // b = {a // b}")
print(f"a ** b = {a ** b}")