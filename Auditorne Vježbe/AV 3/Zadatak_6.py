# Napisati program koji unosi ime i prezime - unosi se u jednu varijablu (imeIPrezime). 
# Ime i prezime treba unijeti razdvojeno jednim razmakom. Program potom provjerava:
# • ako je uneseno i ime i prezime razdvojeno razmakom (odnosno unesen je blanko - razmak), 
#   •Provjerava se da li je uneseno ime Emina, pa ako jeste, ispisuje: Zdravo Emina! . Voditi računa da program 
#   treba prepoznati emina, Emina, eMiNa  itd.
#   •Ako uneseno ime nije Emina, a jeste Edin , onda ispisuje Kako si Edine? .
#   •U suprotnom, ispisuje Dobar dan prezime IME , pri čemu se prezime ispisuje malim slovima, a ime velikim. 
# •Ako nije unesen blanko znak, ali jeste znak * (na bilo kojem mjestu), onda se ispisuju zvjezdice u dužini 
# koliko je uneseno znakova u imeIPrezime. 
# •Ako je pak uneseno —- (tri uzastopna minusa) na bilo kojem mjestu, onda se ispisuje Neispravan unos.
# •Ako nije ništa od gore navedeno, program onda ispisuje Ne sviđaš mi se imeIPrezime, nisi unio razmak.

ime_i_prezime = input("Unesite vase ime i prezime: ")

if " " in ime_i_prezime:
    ime_i_prezime_podijeljeno = ime_i_prezime.split(" ")
    ime = ime_i_prezime_podijeljeno[0]
    prezime = ime_i_prezime_podijeljeno[1]
    if "emina" in ime.lower(): print("Zdravo Emina!")
    elif "edin" in ime.lower(): print("Kako si Edine?")
    else: print(f"Dobar dan {prezime.upper()} {ime.lower()}")
elif " " not in ime_i_prezime and "*" in ime_i_prezime:
    novi_string = "*" * len(ime_i_prezime)
    print(novi_string)
elif "---" in ime_i_prezime:
    print("Neispravan unos.")
else: print(f"Ne svidjas mi se {ime_i_prezime}, nisi unio razmak.")