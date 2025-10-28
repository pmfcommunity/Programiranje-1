# Napisati program koji od korisnika trazi unos broja n.
# Korisnik zatim unosi n brojeva. Program ispisuje razliku najveceg i najmanjeg unesenog broja.

n = int(input("Unesite broj n: "))

i = 0 
lista = []

while i < n:
    k = int(input("Unesite broj k: "))
    lista.append(k)
    i += 1
    
maximum = max(lista)
minimum = min(lista)

print(f"Razlika najveceg i najmanjeg unesenog broja je {maximum - minimum}")