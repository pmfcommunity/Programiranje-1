# Napisati program u koji korisnik unosi 10 cijeli brojeva, svaki u novom redu. Nakon unosa program prvo ispisuje sve negativne brojeve, 
# zatim sve nule i na kraju sve pozitivne brojeve. Unutar svake od grupa broevi trebaju biti u originalnom redoslijedu u ojem su uneseni. 
# Prilikom ispisa brojevi se ispusuju u istom redu a odvojeni su jednim praznim mjestom
# Na primjer, za unesene vrijednosti 3, -4, 8, 0, -1, 0, -6, 1, -1, 0 program treba ispisati:
# -4 -1 -6 -1 0 0 0 3 8 1

pozitivni_brojevi = []
negativni_brojevi = []
nule = []
for _ in range(10): 
    broj = int(input())
    if broj > 0: 
        pozitivni_brojevi.append(broj)
    if broj < 0: 
        negativni_brojevi.append(broj)
    if broj == 0: 
        nule.append(broj)

ispis = ""
    
for broj in negativni_brojevi:
    ispis += str(broj) + " "
for broj in nule:
    ispis += str(broj) + " "
for broj in pozitivni_brojevi:
    ispis += str(broj) + " "
print(ispis)