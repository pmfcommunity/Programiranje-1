# Napisati program koji od korisnika trazi da unese petocifren broj. Program provjerava da li je uneseni broj
# petocifren, te ukoliko jeste, racuna i ispisuje razliku njegove druge najvece i njegove najmanje cifre.

n = int(input("Unesite petocifren broj: "))

if n >= 10000 and n <= 99999:
    desetiljadarka = n // 10000 
    hiljadarka = (n % 10000) // 1000
    stotica = (n % 1000) // 100
    desetica = (n % 100) // 10
    jedinica = n % 10
    
    lista_cifara = [desetiljadarka, hiljadarka, stotica, desetica, jedinica]
    lista_cifara.sort()
    
    druga_najveca = lista_cifara[-2]
    najmanja = min(lista_cifara)
    razlika = druga_najveca - najmanja
    
    print(f"Druga najveca cifra: {druga_najveca}\nNajmanja cifra: {najmanja}")
    print(f"Razlika izmedju druge najvece i najmanje cifre: {razlika}")
else: print(f"Broj {n} nije petocifren!")