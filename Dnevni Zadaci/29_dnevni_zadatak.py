# Napisati program koji od korisnika trazi unos brojeva, sve dok korisnik ne unese broj koji pocinje cifrom 3. Program pronalazi zbir 
# drugog i posljednjeg unesenog broja. Pretpostavite da ce korisnik unijeti bar dva broja. Ukoliko bi korisnik unosio brojeve 12, 43,
# 8, 12, 33, program ce ispisati zbir 33 + 43 = 76. 

lista_brojeva = []
brojac = -1
while True: 
    n = int(input())
    lista_brojeva.append(n)
    brojac += 1
    
    prva_cifra = 0
    while n != 0: 
        prva_cifra = n % 10 
        n //= 10
    if prva_cifra == 3: 
        break 
suma = lista_brojeva[1] + lista_brojeva[brojac]
print(suma)