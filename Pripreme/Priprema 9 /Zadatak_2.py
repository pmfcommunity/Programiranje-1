# Napisati program koji od korisnika uzima neparan broj n. Nakon toga program od korisnika 
# uzima n cijelih brojeva i smjesta ih u listu. Program izbaciju medijanu iz liste i ispisuje listu 
# za n - 1 elemenata u originalnom redoslijedu. Elementi se ispisuju u istom redu razdvojeni praznim mjestom.
# [Napomena: Medijana je broj koji razdvaja gornju polovinu liste od donje, tj. vrijednost koja se nalazi u sredini 
# sortirane liste.]

n = int(input())

if n % 2 == 0: 
    print("")
else: 
    lista_brojeva = []
    originalna_lista = []
    for _ in range(n):
        broj = int(input())
        lista_brojeva.append(broj)
        originalna_lista.append(broj)
    lista_brojeva.sort()
    print(lista_brojeva)
    sredina = len(lista_brojeva) // 2

    ispis = ""
    for broj in originalna_lista: 
        if broj == lista_brojeva[sredina]: continue
        else: 
            ispis += str(broj) + " "
    
    print(ispis)