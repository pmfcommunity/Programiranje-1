# Urediti kod prethodna dva zadatka, tako da dobijete kompletiran kviz koji podsjeća na "Milijunaša". Pitanja se generišu slučajno. 
# Korisnik unosi jednu od opcija (a, b, c ili d), te nastavlja igru sve dok odgovara tačno. Na kraju, program ispisuje ukupan
# broj tačno odgovorenih pitanja.
import random 

brojac_tacnih_odgovora = 0 
brojac_pitanja = 1

for j in range(1, 11):
    a = random.randrange(1, 1000)
    b = random.randrange(1, 1000)
    znak = random.choice("+-*/")

    if znak == "+":
        rezultat = a + b 
    if znak == "-":
        rezultat = a - b 
    if znak == "*":
        rezultat = a * b 
    if znak == "/":
        rezultat = a / b 
        
    tacan_odgovor = round(rezultat, 2) 
    pogresni_prvi = round(rezultat + random.randrange(1, 5), 2)
    pogresni_drugi = round(rezultat + random.randrange(1, 10), 2)
    pogresni_treci = round(rezultat - random.randrange(1, 15), 2) 

    print(f"{brojac_pitanja}. {a} {znak} {b} = ???") 

    odgovori = [tacan_odgovor, pogresni_prvi, pogresni_drugi, pogresni_treci]

    random.shuffle(odgovori)

    brojac = 1
    for odgovor in odgovori: 
        print(f"{brojac}. {odgovor}")
        brojac += 1 
    pokusaj = float(input())
    if pokusaj == tacan_odgovor: 
        tacan_pokusaj = True
        brojac_tacnih_odgovora += 1 
    else: tacan_pokusaj = False

    if tacan_pokusaj: print("Odgovor je tacan.")
    brojac_pitanja += 1

print(f"Tacno ste odgovorili na {brojac_tacnih_odgovora} pitanja.")