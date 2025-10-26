# Napisati program koji od korisnika trazi da unse vrijeme u sekundama. Program treba da pretvori sekunde u sate, 
# minute i sekunda, te ispise vrijednosti.
# B) Ispisati vrijednost sa vodecim nulama (npr. "09:15:08" predstavlja 9 sati, 15 minuta i 8 sekundi.)
# https://samarski.craft.me/2025P1AV2

sekunde = int(input("Unesite vrijeme u sekundama: "))

h = sekunde // 3600
min = (sekunde // 60) % 60
sec = sekunde % 60

print(f"{h:0>2}:{min:0>2}:{sec:0>2}") # Da bi mogao biti ispis imati 0 ako je vremenska jedinica manja od 10.

# 9:15:08 sati je 33308 sekundi.