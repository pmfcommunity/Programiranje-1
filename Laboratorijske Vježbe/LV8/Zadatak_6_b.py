# Napisati funkciju koja vraca listu kombinaciaj od dva elementa. Svaku kombinaciju predstaviti sa posebnom listom od dva elementa. 
# Npr. za listu [1, 2, 3, 4, 5], funkcija vraca [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]

def kombinacije(lista, duzina): 
    lista_permutacija = []
    for i in range(n): 
        for j in range(i + 1, n): 
            permutacija = []
            permutacija.append(lista[i])
            permutacija.append(lista[j])
            lista_permutacija.append(permutacija)
    return lista_permutacija

unos = input()
unos = unos.split(" ")

lista_brojeva = []
for broj in unos: 
    lista_brojeva.append(int(broj))

n = len(lista_brojeva)
print(kombinacije(lista_brojeva, n))