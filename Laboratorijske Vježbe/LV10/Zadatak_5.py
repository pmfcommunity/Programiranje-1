# Napisati funkiciju koja zapisuje matricu u fajl. Koristiti isti format kao zadatak 4. 

def upisi_matricu(fajl):
    matrica = []
    n = int(input("Broj redova: "))
    m = int(input("Broj kolona: "))
    for i in range(n):
        red = []
        for j in range(m):
            red.append(int(input()))
        matrica.append(red)
        print()
    with open(fajl, "x") as f: 
        f.write(str(n) + " " + str(m) + "\n")
        for red in matrica: 
            f.write(" ".join(map(str, red)) + "\n")
        

fajl = "Zadatak_5.txt"
upisi_matricu(fajl)