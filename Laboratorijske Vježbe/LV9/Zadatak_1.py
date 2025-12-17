# Napisati funkciju koja za argument prima listu. Funkcija provjerava da li je proslijedjeni niz u rastucem poretku. 

def rastuci_poredak(lista): 
    jel_rastuci = True 
    sortirana_lista = lista.copy()
    sortirana_lista.sort()
    for i in range(len(lista)):
        if lista[i] != sortirana_lista[i]: 
            jel_rastuci = False 
            break 
    if jel_rastuci: 
        print(f"{lista} je rastuci niz.")
    else: print(f"{lista} nije rastuci niz.")
        

lista_brojeva_1 = [1, 2, 3, 4, 5]
lista_brojeva_2 = [1, 3, 2, 5, 4]
lista_brojeva_3 = [2, 4, 6, 8, 10]
lista_brojeva_4 = [4, 10, 8, 2, 6]

rastuci_poredak(lista_brojeva_1)
rastuci_poredak(lista_brojeva_2)
rastuci_poredak(lista_brojeva_3)
rastuci_poredak(lista_brojeva_4)