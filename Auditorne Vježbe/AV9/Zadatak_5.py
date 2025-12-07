# Napisati funkciju koja za proslijedjene parametre a i b racuna vrijednost izraza a^b. Obratite paznju da parametri a i b mogu
# biti proizvoljni cijeli brojevi. 

def potencija(x, y):
    return x ** y 

a = int(input())
b = int(input())
print(potencija(a, b))