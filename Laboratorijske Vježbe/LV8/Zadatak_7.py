# Napisati program koji ispisuje sve kombinacija od tri elementa. 

unos = input() 
unos = unos.split(" ")

lista_brojeva = []
for broj in unos: 
    lista_brojeva.append(int(broj))
    
n = len(lista_brojeva)

for i in range(n): 
    for j in range(i + 1, n): 
        for k in range(j + 1, n): 
            print(f"{lista_brojeva[i]} {lista_brojeva[j]} {lista_brojeva[k]}")