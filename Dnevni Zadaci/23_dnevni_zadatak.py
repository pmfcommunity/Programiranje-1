# Korisnik unosi visecifreni prirodan broj n. Program ispisuje pretposljednju cifru unesenog broja u vidu teksta. Vrijednost cifre 
# ispisuje se malim slovima, te se ne koriste afrikati. Npr. za broj 123145, ispisuje se "cetiri".

n = int(input())

if n > 0 and n >= 10: 
    pretposljednja = (n % 100) // 10 
    if pretposljednja == 0:
        print("nula")
    elif pretposljednja == 1:
        print("jedan")
    elif pretposljednja == 2:
        print("dva")
    elif pretposljednja == 3:
        print("tri")
    elif pretposljednja == 4:
        print("cetiri")
    elif pretposljednja == 5:
        print("pet")
    elif pretposljednja == 6:
        print("sest")
    elif pretposljednja == 7:
        print("sedam")
    elif pretposljednja == 8:
        print("osam")
    else:
        print("devet")
else: print("Greska! Broj nije prirodan ILI broj je manji od 10")