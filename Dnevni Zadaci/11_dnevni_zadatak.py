# Napisati program koji od korisnika trazi unos petocifrenog prirodnog broja n. Program provjerava da li je uneseni
# broj palindrom. Za broj kazemo da je palindrom, ukoliko se jednako cita sa obje strane. Neki od petocifrenih
# palindroma su 12321, 15651, 92929. Brojevi 12345 ili 12334 nisu palindromi.
# Link zadatka: https://pmfunsaba.sharepoint.com/sites/KN100SIT100-Programiranje12526/Zajednicki%20dokumenti/Dnevni%20zadaci/Zadatak%2011.pdf

print("Unesite petocifreni broj:")
petocifreni = int(input())

if petocifreni >= 10000 and petocifreni <= 99999:
    petocifreni_string = str(petocifreni)
    petocifreni_reversed = "".join(reversed(petocifreni_string))
    if petocifreni_string == petocifreni_reversed:
        print(f"Broj {petocifreni} je palindrom!")
    else: print(f"Broj {petocifreni} nije palindrom!")
else: print("Uneseni broj nije petocifreni.")

# Logika: inace bi se petlja koristila za ovakve zadatke, ali posto do ovog trenutka petlja nije obradjena, 
# koristicemo se stringovima. 
# Ukratko, u Pythonu postoji specijalna funkcija po zvanju "reversed" koja uzima bilo koji tip koji se moze 
# "sijeci" (engl. slice) - tu spadaju nizovi/liste, stringovi, i drugi tipovi. Reversed vraca obrnuti redoslijed 
# stringa, ali vrijednost nije tipa string, vec tipa char. To jest, vraca pojedinacne karaktere stringa.
# Npr. da smo stavili reversed("zdravo") funkcija ne bi vratila "ovardz", vec 'o', 'v', 'a', 'r', 'd', 'z'.
# Da bi dobili string obrnute vrijednosti, moramo koristi funkciju join() koja, po imenu, spaja jedan string sa
# drugim. Koristimo "" da bi vratili povratnu vrijednost funkcije reversed() u string, a oznaka "" znaci da nema 
# prostora izmedju karakterima - tako dobijamo string "ovardz". 