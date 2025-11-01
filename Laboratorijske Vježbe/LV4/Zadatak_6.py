# Napisati program koji trazi od korisnika da unese string. Program ispisuje da li je uneseni string palindrom.

recenica = input("Unesite string: ")

obrnuta_recenica = "".join(reversed(recenica))

jel_palindrom = True 

for i in range(len(recenica)):
    if recenica[i] != obrnuta_recenica[i]:
        jel_palindrom = False
        break 
    
if jel_palindrom: print(f"String {recenica} je palindrom: {obrnuta_recenica}")
else: print(f"String {recenica} nije palindrom: {obrnuta_recenica}")