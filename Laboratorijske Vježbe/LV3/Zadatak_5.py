# Napisati program koji od korisnika trazi da se unese datum - posebno se unosi dan, potom mjesec i na kraju 
# godina. 
# - Ispisati da ji je godina prestupna.
# - Ispisati da li je datum validan. Godina mora biti izmedju 1600 i 2999, mjesec izmedju 1 i 12, a 
#   broj dana u mjesecu zavisi od samog mjeseca: januar, mart, maj, juli, avgust, oktobar i decembar imaju 31
#   dan. April, juni, september, novembar iamju 30 dana, a februar 29 li 28, zavisno od toga da li je u pitanju
#   prestupna godina ili ne respektivno. Na osnovu toga ispisati prigodnu poruku ("datum je validan" ili
#   "godina je van raspona" itd.)
# - Na osnovu unesenog datuma ispisati prvi sljedeci datum u formatu: d. m. g 

print("Unesite datum!")
dan = int(input("Unesite dan: "))
mjesec = int(input("Unesite mjesec: "))
godina = int(input("Unesite godinu: "))

jel_prestupna = False 
ispravna_godina = False 
ispravni_mjesec = False 
ispravni_dan = False 
broj_dana = 0

if godina % 4 == 0:
    if godina % 100 != 0: jel_prestupna = True 
    elif godina % 400 == 0: jel_prestupna = True 

if godina >= 1600 and godina <= 2999: ispravna_godina = True 

if mjesec >= 1 and mjesec <= 12: ispravni_mjesec = True  

if (mjesec == 1 or mjesec == 3 or mjesec == 5 or mjesec == 7 or mjesec == 8 or mjesec == 10 or mjesec == 12) and \
    dan >= 1 and dan <= 31: ispravni_dan = True 
elif (mjesec == 4 or mjesec == 6 or mjesec == 9 or mjesec == 11) and dan >= 1 and dan <= 30: ispravni_dan = True 
elif mjesec == 2: 
    if jel_prestupna and dan >= 1 and dan <= 29: ispravni_dan = True 
    if not jel_prestupna and dan >=1 and dan <= 28: ispravni_dan = True 
else: ispravni_dan = False 

if ispravni_dan and ispravni_mjesec and ispravna_godina: 
    print("Datum je ispravan!")
    print(f"{dan}.{mjesec}.{godina}.")
else: print("Datum nije ispravan!")