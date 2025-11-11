n = int(input())
lista_cifara = []

i = 1
while i <= n:
    cifra = int(input())
    lista_cifara.append(cifra)
    i += 1
    
lista_vecih = []

for i in range(1, n - 1):
    if lista_cifara[i] > lista_cifara[i + 1] and lista_cifara[i] > lista_cifara[i - 1]:
        lista_vecih.append(lista_cifara[i])

for cifra in lista_vecih:
    print(cifra, end=" ")
