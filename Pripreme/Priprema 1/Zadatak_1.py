# Napisati prgoram koji pretvara iznos novca iz eura u drugu valutu. Korisnik prvo unosi iznos novca u eurima,
# a zatim valutu u koju zelida konvertuje: dolare (USD), britanske funte (GBP), ili japanske jene (JPY). 
# Kursne vrijednosti su unaprijed definisane: 
# - 1 EUR = 1.06 USD
# - 1 EUR = 0.83 GBP
# - 1 EUR = 164.3 JPY

euri = float(input())
valuta = input()

nova_valuta = 0
if valuta.lower() == "usd":
    nova_valuta = euri * 1.06 
    print(nova_valuta)
elif valuta.lower() == "gbp":
    nova_valuta = euri * 0.83
    print(nova_valuta)
elif valuta.lower() == "jpy":
    nova_valuta = euri * 164.3
    print(nova_valuta)
else: print("Greska!")