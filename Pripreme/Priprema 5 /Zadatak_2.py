# Napisati program koji od korisnika trazi unos broja n, a zatim n cijelih brojeva jedan ispod drugog. Za svaki uneseni broj 
# program treba ispisati sumu svih ostalih brojeva osim tog broja. Rezultati se ispisuju svaki u zasebnom redu.

n = int(input())
lista_brojeva = []

for i in range(n):
    broj = int(input())
    lista_brojeva.append(broj)

suma = 0
for broj in lista_brojeva: 
    suma += broj 

lista_ostalih_suma = [] 
for broj in lista_brojeva: 
    print(suma - broj)