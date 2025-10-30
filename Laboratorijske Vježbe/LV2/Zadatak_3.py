# Napisati program koji od korisnika trazi da unese velicinu ugla u sekundama. Program treba da sekunde pretvori
# u stepene, minute, i sekunde, te ispiste te vrijednosti.

sekunde = int(input("Unesite velicinu ugla u sekundama: "))

stepeni = sekunde // 3600
minute = (sekunde % 3600) // 60
sekunde = sekunde % 60

print(f"{stepeni:0>2}:{minute:0>2}:{sekunde:0>2}")