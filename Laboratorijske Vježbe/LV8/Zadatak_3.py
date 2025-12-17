# Napisati funkciju centrirani_ispis koja kao parametar prima tekst (string)m i ispisuje tekst centrirano sa crtciama sa lijeve i desne
# strane, sa ukupnom duzinom od 80 karaktera. Na primjer, za tekst "kraj" funkcija ispisuje "--- kraj ---" sa ukupnom duzinom od 80
# karaktera. Prije prvog slova k i zadnjeg slova j se nalazi jedan razmak. 

def centrirani_ispis(tekst):
    formatirani_tekst = f" {tekst} "
    ispis = formatirani_tekst.center(80, "-")
    print(ispis)

tekst = input()
centrirani_ispis(tekst)