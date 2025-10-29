# Program od korisnika trazi da unese sest cijelih brojeva koji predstavljaju koordinate vrhova trougla u ravni.
# Prva dva broja su koordinate x i y za prvu, iduca dva za drugu i posljednja dva za trecu tacku. Program 
# provjerava da li su unesene tacke kolinearne. Ako jesu, program ispisuje odgovarajucu poruku i ne radi vise nista.
# Ukoliko tacke nisu kolinearne, one cine trougao. Nakon toga, od korisnika se ocekuje da unese koordinate jos 
# jedne tacke u ravni, te provjerava da li se unesena tacka nalazi u trouglu.

print("Unesite koordinate za prvu tacku: ")
x1 = int(input())
y1 = int(input())

print("Unesite koordinate za drugu tacku: ")
x2 = int(input())
y2 = int(input())

print("Unesite koordinate za trecu tacku: ")
x3 = int(input())
y3 = int(input())

povrsina = 1 / 2 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

if int(povrsina) == 0:
    print("Tacke su kolinearne")
else:
    print("Tacke nisu kolinearne, unesesite koordinate za cetvrtu tacku: ")
    x4 = int(input())
    y4 = int(input())
    
    povrsina1 = 1 / 2 * abs(x4 * (y2 - y3) + x2 * (y3 - y4) + x3 * (y4 - y2))
    povrsina2 = 1 / 2 * abs(x1 * (y4 - y3) + x4 * (y3 - y1) + x3 * (y1 - y4))
    povrsina3 = 1 / 2 * abs(x1 * (y2 - y4) + x2 * (y4 - y1) + x4 * (y1 - y2))
    
    if abs(povrsina - (povrsina1 + povrsina2 + povrsina3)) < 0.000000001:
        print("Cetvrta tacka se nalazi unutar trougla.")
    else: print("Cetvrta tacka se ne nalazi unutar trougla.")