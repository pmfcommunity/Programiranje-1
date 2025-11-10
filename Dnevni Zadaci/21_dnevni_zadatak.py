# Napisati program koji simulira bacanje novcica. Korisnik bira jedan od brojeva 0 (glava) ili 1 (pismo). Program slucajno generise 
# jedan od ishoda, te ukoliko je korisnik ispravno pogadao, program trazi novi unos. Nakon sto korisnik ne pogodi ishod bacanja, program
# prekda sa radom i ispisuje broj pogodjenih bacanja. 

import random
broj_pogodjenih_bacanja = 0 

while True : 
    print("Pogodite stranu novcica: ")
    pogodak_korisnika = int(input())
    pogodak_robota = random.randint(0, 1)
    
    if pogodak_korisnika == pogodak_robota:
        print(f"Vas pogodak: {pogodak_korisnika}")
        print(f"Izabir robota: {pogodak_robota}")
        print("Tacno!\n")
        broj_pogodjenih_bacanja += 1
    else: 
        print(f"Vas pogodak: {pogodak_korisnika}")
        print(f"Izabir robota: {pogodak_robota}")
        print("Ne tacno!\n")
        break 
print(f"Broj tacnih pogadjaja: {broj_pogodjenih_bacanja}")