# Napisati funkciju koja prihvata prirodan broj n kao parametar. Funkcija ispisuje n-ti Fibonaccijev broj. 

def fibonaccijev_broj(x): 
    a, b = 0, 1 
    brojac = 1 
    while brojac < x: 
        c = a + b 
        a = b 
        b = c 
        brojac += 1 
    return a

n = int(input())
if n < 0: print("Broj mora biti prirodan.")
else: 
    print(fibonaccijev_broj(n))    