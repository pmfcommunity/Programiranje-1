# Napisati program koji trazi od korisnika da unese dva realna broja x i y, i operaciju sabiranja, oduzimanja,
# mnozenja, dijeljenja i modularnog dijeljenja. Program ispisuje rezultat, i adektvatnu poruku za neispravan
# unos.

x = float(input("Unesite x: "))
y = float(input("Unesite y: "))
operacija = input("Unesite operaciju: ")

rezultat = 0
ispravan_unos = True
match operacija:
    case "+":
        rezultat = x + y 
    case "-":
        rezultat = x - y 
    case "*":
        rezultat = x * y 
    case "/":
        rezultat = x / y 
    case "%":
        rezultat = x % y 
    case "mod" :
        rezultat = x % y 
    case _: 
        print("Ne isravan unos operacije!")
        print("Podrzane operacije: +, -, *, /, % (mod)!")
        ispravan_unos = False 
if ispravan_unos: print(f"Rezultat {x} {operacija} {y} = {rezultat}")