# Napisati program koji od korisnika trazi da unese cetverocifren broj. Program provjerava da li je uneseni broj
# cetverocifren, te ispisuje njegovu najvecu cifru. 

cetverocifreni = int(input("Unesite cetverocifreni broj: "))

if cetverocifreni >= 1000 and cetverocifreni <= 9999:
    hiljadarka = cetverocifreni // 1000
    stotica = (cetverocifreni // 100) % 10
    desetica = (cetverocifreni // 10) % 10
    jedinica = cetverocifreni % 10
    maximum = max(hiljadarka, stotica, desetica, jedinica)
    print(f"Najveca cifra broja {cetverocifreni} je {maximum}")
else: print("Broj nije cetverocifren!")