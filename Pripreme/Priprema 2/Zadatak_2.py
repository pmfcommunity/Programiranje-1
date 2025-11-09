# Video objavljen na drustvenim mrezama postaje viralan. Broj pregleda raste za 10% svakog sata. Potrebno je odrediti za koliko ce 
# sati broj pregleda premasiti odredjeni prag. 
# Program prvo zahtijeva unos pocetnog broja pregleda, a zatim ciljni broj pregleda. Nakon toga, racuna koliko sati je potrebno da
# broj pregleda premasi zadanu vrijednost i ispinsuje taj broj.
# Na primjeru ispod, pocetni broj pregleda je 100, a ciljni prag 150. broj pregleda raste na sljedeci nacin:
# 100 -> 110 -> 133.1 -> 146.41 -> 161.05. Nakon petog sata, broj pregleda prelazi zadani prag, pa je ispis 5. 

pocetni_broj = int(input())
ciljni_prag = int(input())

brojac = 0
while pocetni_broj <= ciljni_prag: 
    pocetni_broj += (pocetni_broj * (0.10))
    brojac += 1
print(brojac)