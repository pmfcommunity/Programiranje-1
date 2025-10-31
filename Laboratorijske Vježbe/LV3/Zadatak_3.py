# Napisati program koji unosi string. Od korisnika se ocekuje da unese tri rijeci, razdojene po jednim blank
# (razmak) karakterom. 
# - Program treba da ispise svaku rijec, po jednu u svakom redu, redom kako su napisane. 
# - Program da ispise svaku rijec, slozeno po velicini

recenica = input("Unesite string sa tri rijeci: ")

pronadji_razmak_1 = recenica.find(" ")
prva_rijec = recenica[0:pronadji_razmak_1]

nakon_prve_rijeci = recenica[pronadji_razmak_1 + 1:]
pronadji_razmak_2 = nakon_prve_rijeci.find(" ")

druga_rijec = nakon_prve_rijeci[:pronadji_razmak_2]
treca_rijec = nakon_prve_rijeci[pronadji_razmak_2 + 1:]

print(prva_rijec)
print(druga_rijec)
print(treca_rijec)

lista_rijeci = [prva_rijec, druga_rijec, treca_rijec]

sortirane_rijeci = sorted(lista_rijeci, key=len)

prva_najveca = sortirane_rijeci[0]
druga_najveca = sortirane_rijeci[1]
treca_najveca = sortirane_rijeci[2]

print("Rijeci sortirane po velicini:")
print(prva_najveca)
print(druga_najveca)
print(treca_najveca)