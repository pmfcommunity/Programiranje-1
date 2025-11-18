# Napisati program koji od korisnika traži da unosi prirodne brojeve sve dok ne unese broj 100. 
# Program ispisuje unesene brojeve u obrnutom poretku.

lista_brojeva = []

while True: 
    x = int(input())
    if x == 100: 
        break 
    lista_brojeva.append(x)

lista_brojeva.reverse()
for lista in lista_brojeva:
    print(lista, end=" ")
print("")