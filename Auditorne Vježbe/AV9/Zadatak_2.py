# Napisati funkciju koja za proslijedjenu listu cijelih brojeva vraca element sa najvecom sumom cifara. 

def suma_cifara(lista): 
    lista_sume = []
    for broj in lista: 
        kopija = broj 
        suma = 0 
        while kopija != 0: 
            cifra = kopija % 10 
            suma += cifra 
            kopija //= 10 
        lista_sume.append(suma)
    return max(lista_sume)

print(suma_cifara([123, 2321, 1123]))