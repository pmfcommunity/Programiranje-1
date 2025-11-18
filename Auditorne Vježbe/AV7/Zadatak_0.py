# Uvodne stvari
# Sabiranje listi
# Dodavanje elementa
# Brisanje elementa
# Indeksni pristup - jedan element i opseg
# Dodjela: x, y = lista
# Otpakivanje listi
# Dodjela: x, *y = lista
# Dodjela: _ (nekorištena vrijednost)

# Sabiranje listi
lista_1 = [0, 1, 2]
lista_2 = [3, 4, 5]
suma = 0 
for i in range(len(lista_1)):
    suma += lista_1[i] + lista_2[i]
print(suma)

# Dodavanje elementa 
print()
print(lista_1, len(lista_1)) 
lista_1.append(3)
lista_1.append(4)
lista_1.append(5)
print(lista_1, len(lista_1))

# Brisanje elementa
print()
print(lista_1)
lista_1.remove(4)
print(lista_1)

# Indeksi pristup
print()
print(lista_1.index(2))

# Dodjela 
print()
lista_3 = lista_1 + lista_2 
print(lista_1, lista_2)
print(lista_3)

# Otpakivanje
print()
a, b, c = lista_2
print(lista_2)
print(a, b, c) 

# Dodjela x * y 
print()
lista_4 = lista_1 * 3
print(lista_4)