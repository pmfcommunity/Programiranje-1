# Korisnik unosi visecifren prirodan broj. Program ispisuje razlku proizvoda i kolicnika najvece i najmanje cifre broja. 
# Za broj 27385, ispisuje broj 12. 

n = int(input())

lista_cifara = []
while n != 0: 
    cifra = n % 10
    lista_cifara.append(cifra)
    n //= 10 
najveca_cifra = max(lista_cifara)
najmanja_cifra = min(lista_cifara)

proizvod = najveca_cifra * najmanja_cifra
kolicnik = najveca_cifra / najmanja_cifra 
razlika = proizvod - kolicnik
print(razlika)