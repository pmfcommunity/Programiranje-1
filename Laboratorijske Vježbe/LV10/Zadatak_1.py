# Napisati program koji od korisnika trazi unos naziva fajla. Program cita kompletan fajl i ispisuje ukupan broj recenica. 

fajl = input()
with open(fajl, "r") as f:
    brojac = 0
    for red in f: 
        red = red.strip()
        sadrzaj = red.split(" ")
        for rijec in sadrzaj:
            brojac += 1 
    print(brojac)