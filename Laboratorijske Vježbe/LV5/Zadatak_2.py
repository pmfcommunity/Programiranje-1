# Napisati program koji ispisuje ASCII tablicu. Karakteri su ispisani po 16 u svakom redu (ukupno 7 redova), sa jednim razmakom izmedju.
# Na pocetku svakog reda se ispisuje kod prvog znaka u tom redu, znakovi su poredani od prvog (kod 32) do posljednjeg vidljivog (kod 126)

ascii_kod = chr(32)
kod = 32 
for i in range(6):
    print(f"{kod:<5} ", end="")
    for j in range(16):
        print(ascii_kod, end=" ")
        temp = ord(ascii_kod)
        sljedeca = temp + 1 
        ascii_kod = chr(sljedeca)
        kod += 1
    print()