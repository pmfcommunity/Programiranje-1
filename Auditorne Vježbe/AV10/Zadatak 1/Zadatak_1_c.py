# Napisati funkciju koja prima prirodan broj n, te u fajl pod nazivom "brojevi.txt" upisuje prvih n prirodnih brojeva, jedan ispod 
# drugog. 

def upis_brojeva(n): 
    fajl = "Zadatak_1_c.txt"
    with open(fajl, "x") as f: 
        for i in range(1, n + 1): 
            f.write(str(i))
            f.write("\n")

x = int(input())
upis_brojeva(x)