# Napisati funkciju koja proslijedjeni string "centrira" na proslijedjeni maksimalni broj znakova, na nacin da se i sa lijeve i sa 
# desne strane ubai prazan znak (razmak). U slucaju da je string duzi od predvidjenog broja znakova, string se skracuje (sa kraja)
# na predvidjeni broj znakova. Primjer poziva funkcije: cenriraj("Naslov", 80)
# Dodati defaultnu vrijednost za drugi parametar, da bude 80

def centriraj(tekst, razmak=80):
    if len(tekst) > razmak: 
        tekst = tekst[:razmak]
    broj_razmaka = razmak - len(tekst)
    lijevo = broj_razmaka // 2 
    desno = broj_razmaka - lijevo
    return " " * lijevo + tekst + " " * desno 

string = "Naslov"
print(centriraj(string))