# Napisati program koji od korisnika trazi unos cijelih brojeva, sve dok se 
# une unese rijec kraj (nije vazno da li je napisano Kraj, kRAj ili KRAJ), cime se
# oznacava zavrsetak unosa. Program ispisuje sumu unesenih brojeva.

suma = 0
while True:
    n = int(input("Unesite broj n: "))
    suma += n 
    kraj = input("Unesite 'kraj' za zavrsetak unosa: ")
    if kraj.lower() == "kraj": break

print(f"Suma unesenih brojeva iznosi: {suma}")