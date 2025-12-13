# Napisati program koji ispisuje sumu brojeva koji su zapisani u fajlu "brojevi.txt". Svaki broj je zapisan u posebnom redu. 
# Dodatno, na kraju fajla dodati (zapisati) ukupnu sumu.

fajl = "Zadatak_1_a.txt"
suma = 0 
with open(fajl, "r") as f: 
    for linija in f: 
        broj = int(linija.strip())
        suma += broj 
    print(suma)
    
with open(fajl, "a") as f:
    f.write("\n") 
    f.write(str(suma))
    print("Dodano!")
f.close()