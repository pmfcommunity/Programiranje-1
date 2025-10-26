# a) Napraviti program koji od korisnika trazi da se unese ime, i potom ispisuje ime formatirano na razlicite nacine.
# Na primjer, ako korisnik unese ime "Emir", tada se ispisuje (tacka predstavlja oznaku za razmak): 
# https://samarski.craft.me/2025P1AV2

ime = input("Unesite vase ime: ")

# Prema ispisu, ima duzinu od 10 karaktera. 

print(f"{ime:.<10}")
print(f"{ime:.>10}")
print(f"{ime:.^10}")
print(f"{ime:*^10}")

# . i * - karaktere koje hocemo da stavimo uprazan prostor.
# < - hocemo da stavimo varijablu na pocetak ispisa, i popuniti ostali prazan prostor izabranim karakterom.
# > - hocemo da stavimo varijablu na kraj ispisa, i popuniti ostali prazan prostor izabranim karakterom.
# ^ - hocemo da stavimo varijablu u sredinu ispisa, i popuniti ostali prazan prostor izabranim karakterom.

# b) Napraviti program koji od korisnika trazi da se unese iznos, i potom ispisuje na ekranu iznos, na dvije 
# decimale, sa vodecm zvjezdicama, sa ukupno 15 mjesta.
print() # Nije potrebno, samo se dodaje jos jedna nova linija. Korisno za preglednost.
# Isto kao da smo napisali print("")

iznos = float(input("Unesite neki broj: "))
print(f"{round(iznos, 2):*>15}")

# round(varijabla, broj_decimala) - prvi argumenat je varijabla tipa float, a drugi argumenat je koliko zelimo 
# decimalnih mjesta da zaokruzimo broj.