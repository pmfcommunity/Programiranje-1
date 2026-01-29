# Napisati funkciju koja privhata listu. Funkcija mijenja svaki element liste najvecim elementom u listi sa 
# njegove desne strane. Posljedni element liste mijenja se brojem -1. Ukoliko je data lista [17, 18, 5, 4, 6, 1]. 
# rezultujuca lista je [18, 6, 6, 6, 1, -1]

def sortirana_lista(lista):
    for i in range(len(lista) - 1):
        nova_lista = lista[i+1:len(lista)]
        najveci = max(nova_lista)
        lista[i] = najveci
    lista[-1] = -1
    print(lista)

n = int(input())
niz = []

for _ in range(n):
    niz.append(int(input()))
    
sortirana_lista(niz)