# Napisati program koji zahtijeva unos prirodnog broja n, i kojim se potom unosi n cijelih brojeva. 
# Program provjerava da li među tim brojevima postoje takva 3 da je treći zbir prva dva.

n = int(input())

lista_brojeva = []
for i in range(n): 
    x = int(input())
    lista_brojeva.append(x)
    
postoji_li = False 

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and i != k and j != k: 
                if lista_brojeva[j] == lista_brojeva[i] + lista_brojeva[j]:
                    postoji_li = True 

if postoji_li: 
    print("Postoji tavka trojika.")
else: print("Ne postoji takva trojika.")