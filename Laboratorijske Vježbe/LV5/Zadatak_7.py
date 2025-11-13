# Napisati program koji u unesenom broju n trazi da li postoji cifra nula pocevsi od jedinica (dakle, sa desne strane). Ukoliko postoji
# program treba da napise "Postoji" i potom ispise broj n u kojem je nadjena cifra nula zamijenjena cifrom jedan. U suprotnom, program
# ispisuje poruku "Ne postoji". Nije dozvoljeno koristiti operacije sa stringovima! 
# Na primjer, za uneseni broj 12305 program treba da ispise "Postoji" i potom "12315"

n = int(input())
da_li_nula_postoji = False 
kopija = n 

pozicija = -1
while kopija != 0: 
    cifra = kopija % 10 
    if cifra == 0: 
        da_li_nula_postoji = True 
        break 
    pozicija -= 1 
    kopija //= 10 

if da_li_nula_postoji:
    broj_u_string = ""
    kopija = n 
    lista_cifara = []
    
    while kopija != 0: 
        cifra = kopija % 10
        lista_cifara.append(cifra)
        kopija //= 10
    lista_cifara.reverse()
    lista_cifara[pozicija] = 1
    
    for broj in lista_cifara: 
        broj_u_string += str(broj)
    print("Postoji")
    print(int(broj_u_string))
else: print("Ne postoji")        