# Napisati program koji od korisnika trazi unos dva broja i smjesta ih u varijable a i b, redom. Program 
# mijenja vrijednosti koje se nalaze u varijablama (swap).

# 1. Nacin

a = int(input("Unesite prvi broj a: "))
b = int(input("Unesite drugi broj b: "))

print(f"Prije izmjene: {a}, {b}")
a, b = b, a 
print(f"Nakon izmjene: {a}, {b}")
print()

# 2. Nacin

a = int(input("Unesite prvi broj a: "))
b = int(input("Unesite drugi broj b: "))

print(f"Prije izmjene: {a}, {b}")
temp = a 
a = b
b = temp  
print(f"Nakon izmjene: {a}, {b}")