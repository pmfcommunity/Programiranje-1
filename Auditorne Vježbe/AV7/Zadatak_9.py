# Napisati program koji unosi recenicu (rijecu su odvojene praznim znakom - razmakom). Program nalazi najduzu rijec u recenici.
recenica = input()
lista_rijeci = recenica.split(" ")

najduza = max(lista_rijeci, key=len)
print(najduza)