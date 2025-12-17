# Napisati program koji unosi recenicu (rijecu su odvojene praznik znakom - razmakom). Program nalazi najduzu rijec u recenici.

recenica = input()

recenica = recenica.split(" ")

najduza = ""
for rijec in recenica: 
    if len(rijec) > len(najduza):
        najduza = rijec 

print(najduza)