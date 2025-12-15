# Napraviti unos dva datuma. Program zatim ispisuje sve datume koji se nalaze između dva unesena datuma.

from datetime import datetime, timedelta

datum_1 = input()
od_datuma = datetime.strptime(datum_1, "%d.%m.%Y")

datum_2 = input()
do_datuma = datetime.strptime(datum_2, "%d.%m.%Y")

dan = timedelta(days = 1)
datum = od_datuma

while datum <= do_datuma: 
    print(f"{datum:%#d.%#m.%#Y}")
    datum += dan