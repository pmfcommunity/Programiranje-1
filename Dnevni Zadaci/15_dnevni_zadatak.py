# Kreirati program koji ce simulirati rad bankomata. Program na pocetku ispisuje pozdravnu poruku i od korisnika
# trazi da unese sifru. Sifra je cetverocifreni prirodan broj. Program samo provjerava da li je sifra cetverocifren
# broj, te ukoliko jeste, korisniku je dozvoljen pristup (nema detaljnije provjere). Nakon "ulaza u sistem", 
# program korisniku nudi vise opcija:
# 1. Pregled stanja - 2. Uplata - 3. Isplata - 4. Izlaz
# Opcije su oznaceve brojevima (1-4), te unos broja opcije usmjerava korisnika. Unos koji nije u navedenom opsegu
# prekida program.
# "Pregled stanja" ispisuje trenutno stanje na racunu (pretpostavimo da korisnik u pocetku ima 8550 novcanih
# jedinica).
# "Uplata" omogucava korisniku da uplati iznos do 2000 novcanih jedinica. Vece uplate i uplate manje od 0 nisu 
# dozvoljene. Program ispisuje prikladnu poruku u slucaju nepravilnog unosa. Ukoliko je unos zadovoljavajuci, 
# korisnik ima pravo da izabere dvije opcije 'D' ili 'N', kao odgovor na pitanje: "Zelite li prikaz konackog stanja?"
# Ukoliko korisnik izabere prvu opciju, prikazano je stanje racuna nakon uplate. 
# "Isplata" omogucava korisniku da podigne novac. Korisnik smije podici 500 novcanih jedinica vise od trenutnog 
# stanja na racunu. Vrijednost mora biti djeljiva sa 100. Program ispisuje stanje racuna nakon izvrsene transakcije.
# U slucaju pogresnog unosa, program javlja gresku.
# "Izlaz" samo ispisuje pozdravnu poruku i zahvaljuje korisniku na koristenju usluga. 

print("Dobro dosli na PMF Bank!")
print("Unesite vas PIN: ", end="")
pin = int(input())

if pin >= 1000 and pin <= 9999:
    print("Ulaz dozvoljen! Dobro dosli u sistem.\n")
    print("Izaberite opciju od (1-4):")
    print("1. Pregled stanja")
    print("2. Uplata")
    print("3. Isplata")
    print("4. Izlaz")
    odluka = int(input())
    
    novcane_jedinice = 8550
    
    match odluka:
        case 1: 
            print(f"Vase trenutno stanje na racunu iznosi: {novcane_jedinice}KM.")
        case 2:
            print("Unesite iznos za uplatu: ", end="")
            uplata_novca = int(input())
            if uplata_novca >= 0 and uplata_novca <= 2000:
                novcane_jedinice += uplata_novca
                print("Novac uplacen! Zelite li prikaz konacnog stanja? (D ili N)")
                odgovor_stanja = input()
                if odgovor_stanja.upper() == "D":
                    print(f"Vase trenutno stanje na racunu iznosi: {novcane_jedinice}KM.")
                elif odgovor_stanja.upper() == "N":
                    print("Hvala na povjerenju!")
                else: print("Ne pravilan unos!")
            else: print("Ne pravilan unos! Novac ne moze biti negativan, ili veci od 2000km.")
        case 3:
            print("Unesite iznos za podizanje novca: ", end="")
            novac_za_podizanje = int(input())
            limit = 500
            if novac_za_podizanje % 100 == 0 and novac_za_podizanje <= novcane_jedinice + limit:
                novcane_jedinice -= novac_za_podizanje
                print(f"Vase trenutno stanje na racunu iznosi: {novcane_jedinice}KM.")
            else: print("Ne pravilan unos! Iznos mora biti djeljiv sa 100 ili ste prekoracili granicu! (najvise 500KM vise od trenutnog stanja)")
        case 4:
            print("Hvala na povjerenju!")
else: print("Pogresan PIN! Pristup odbijen.")