# Napisati funkciju koja za argument prima listu. Funkcija vraca listu koja je nastala od proslijedjene liste u kojoj je svaki element 
# pomnozen sa 2, ali tako da se proslijedjena lista ne mijenja. 

def pomnozak(lista): 
    nova_lista = lista.copy()
    for i in range(len(nova_lista)): 
        nova_lista[i] *= 2
    print(nova_lista)
    print(lista)

n = int(input())
lista_brojeva = []

for _ in range(n): 
    lista_brojeva.append(int(input()))
    
pomnozak(lista_brojeva)