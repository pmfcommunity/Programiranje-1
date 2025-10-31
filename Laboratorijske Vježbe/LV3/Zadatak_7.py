# Napisati program koji od korisnika trazi da unese trocifreni broj. Program provjerava da li je uneseni broj
# trocifren, te ukoliko jeste, racuna i ispisuje proizvod njegovih cifara.

n = int(input("Unesite trocifreni broj: "))

if n >= 100 and n <= 999: 
    stotica = n // 100 
    desetica = (n % 100) // 10 
    jedinica = n % 10 
    proizvod = stotica * desetica * jedinica 
    
    print(f"Cifre broja {n}: {stotica}, {desetica}, {jedinica}")
    print(f"Proizvod cifara: {proizvod}")
else: print(f"Broj {n} nije trocifren!")