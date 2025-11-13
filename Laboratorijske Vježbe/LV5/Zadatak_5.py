# Napisati program koji za unesene prirodne brojeve n i m provjerava da li se unutar n bacanja kocice (koja ima stranice sa brojevima
# 1 do 6), koristeci slucajne brojeve (random.randint) pojavilo m uzastopnih sestica. 
# Potopm napisati program koji prvo unosi broj k, a potom n i m, i koji provjerava koliko se puta unutar k simulacija od n uzastopnih
# bacanja kockike pojavilo m uzastopnih sestica, i to koristiti da se izracuna vjerovatnoca ovog dogadjaja.

from random import randint

k = int(input())
n = int(input())
m = int(input())

uzastopnih_sestica = 0
koliko_sestica = 0
for j in range(k):
    for i in range(n): 
        kockika = randint(1, 6)
        if kockika == 6: uzastopnih_sestica += 1
        else: uzastopnih_sestica = 0
        if uzastopnih_sestica == m: 
            koliko_sestica += 1 
            break
vjerovatnoca = (koliko_sestica / k) * 100
print(f"Broj uzastopnih sestica: {koliko_sestica}")
print(f"Vjerovatnoca ovog dogadjaja: {vjerovatnoca}%")