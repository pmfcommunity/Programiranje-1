# Napisati program koji od korisnika razi unos recenice. Program provjerava da li je unesena recenica palindrom. 

recenica = input()

bez_razmaka = ""
for i in range(len(recenica)):
    if recenica[i] == " ": continue
    else: bez_razmaka += recenica[i]

if bez_razmaka == bez_razmaka[::-1]:
    print("Unesena recenica je palindrom")
else: print("Unesena recenica nije palindrom")