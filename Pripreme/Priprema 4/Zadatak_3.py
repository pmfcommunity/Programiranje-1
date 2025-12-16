# Grupa od n prijatelja planira otici u kino i zele pronaci prostor gdje mogu sjediti jedni pored drugih u istom redu. Raspored sjedista
# u kinu moze se predstaviti kao dvodimenzionalna matrica, gdje 0 oznacava prazno sjediste, a 1 zauzeto sjediste. 
# Korisnik u prom redu unosi broj prijatelja n, dok u narednim redovima unosi raspored kina. Unos zavrsava praznim redom. 
# Program treba izracunati i ispisati ukupan broj dostupnih prostora na kojima svih n prijatelja mogu sjediti zajedno 

n = int(input())
matrica = []
while True: 
    linija = input()
    if linija == "":
        break 
    matrica.append([int(x) for x in linija.split(" ")])
    
brojac = 0

for red in matrica: 
    for p in range(0, len(red) - n + 1):
        if red[p:p + n] == [0] * n: 
            brojac += 1 
            
print(brojac)