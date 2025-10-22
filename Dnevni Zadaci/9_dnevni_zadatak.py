# Napisati program koji trazi da se sa tastature unesu dva vremenska trenutka, u satima, minutama i sekundama.
# Program racuna i ispisuje vrijeme koje je proteklo izmedju ta dva vremenska perioda. Ispis treba takodjer biti u 
# satima, minutama i sekundama. Pretpostaviti da je drugi vremenski period uvijek nakon prvog. Jedan od mogucih
# dijaloga nakon pokretanja je naveden u PDF postavke zadatka:
# https://pmfunsaba.sharepoint.com/sites/KN100SIT100-Programiranje12526/Zajednicki%20dokumenti/Dnevni%20zadaci/Zadatak%209.pdf

print("Unesite vrijeme 1 (h min sec):")
h1 = int(input())
min1 = int(input())
sec1 = int(input())

print("Unesite vrijeme 2 (h min sec):")
h2 = int(input())
min2 = int(input())
sec2 = int(input())

# Jedan od mogucih nacina jeste da prvo pretvorimo oba vremenska trenutka u sekunde. 

trenutak1 = h1 * 3600 + min1 * 60 + sec1
trenutak2 = h2 * 3600 + min2 * 60 + sec2

# Ovdje bi inace radili komparaciju putem "if else" naredbe. Ali zbog postavke, i posto su ovo zadaci koji se rade
# prije ovog gradiva, preptostavlja se da je drugi trenutak veci od prvog. 
# Ali, ovaj zadatak ce se uraditi preko "if else" naredbe.

if trenutak1 > trenutak2:
    razlika = trenutak1 - trenutak2
else: razlika = trenutak2 - trenutak1

# Logika: ako je prvi vremenski trenutak strogo veci od drugog, onda cemo prvo oduzimati trenutak 1 (vecim) sa 
# trenutkom 2 (manjim), ako prvi vremenski trenutak nije veci od drugog, onda se pretpostavlja da je on manji, pa 
# se oduzima prvo trenutak 2 sa trenutkom 1. 
# Inace bi samo islo "razlika = trenutak2 - trenutak1" - prema postavci zadatka. 

# Formula za pretvaranje vremenskog trenutka u sekudama u sate, minute, i u sekunde:
h = razlika // 3600
min = (razlika % 3600) // 60
sec = razlika % 60

print('-'*50)
print("Izmedju ova dva trenutka je proteklo:")
print(f"{h} h {min} min i {sec} sec.")