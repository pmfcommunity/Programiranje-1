# Napraviti program koji od korisnika trazi da se unese ime, i potom ispisuje ime formatirano na razlicite nacine.
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