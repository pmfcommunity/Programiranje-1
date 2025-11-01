# Korisnik unosi pozitivne brojeve jedan ispod drugog. Kraj unosa korisnik oznacava sa -1. Program ispisuje sumu
# posljednjih cifara unesenih brojeva. 

suma_posljednjih_cifara = 0 
while True: 
    n = int(input("Unesite pozitivni broj: "))
    if n > 0: 
        suma_posljednjih_cifara += n % 10 
    else: break 

print(f"Suma posljednjih cifara unesenih brojeva: {suma_posljednjih_cifara}")