# Za prirodan broj kazemo da je fin ako sadrzi dvije uzastopne cifre cija je suma jednaka 4. Korisnik unosi prirodan broj n. Program 
# ispisuje da li je n fin broj. 

n = int(input())
kopija = n

jel_fin = False
while kopija // 10 != 0:
    prva_cifra = kopija % 10
    sljedeca_cifra = (kopija % 100) // 10
    
    if prva_cifra + sljedeca_cifra == 4:
        jel_fin = True 
        break     
    
    kopija //= 10 
if jel_fin: print(f"Broj {n} je fin.")
else: print(f"Broj {n} nije fin.")