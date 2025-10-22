# Napisati program koji u konzoli ispisuje oblik koji podsjeca na izgled zastave Bosne i Hercegovine. Umjesto plave
# boje se ispisuje znak "-", umjest zute "3", te umjesto bijele "x".
# Link zadatka: https://pmfunsaba.sharepoint.com/sites/KN100SIT100-Programiranje12526/Zajednicki%20dokumenti/Dnevni%20zadaci/Dnevni%20zadatak%205.pdf

# PRVI NACIN (Samo ispis)
print("---------x-333333--")
print("----------x-33333--")
print("-----------x-3333--")
print("------------x-333--")
print("-------------x-33--")
print("--------------x-3--")

# DRUGI NACIN (Bez rucnog pisanja minusa)
print(f"{'x-333333--':->17}--")
print(f"{'x--33333--':->17}--")
print(f"{'x---3333--':->17}--")
print(f"{'x----333--':->17}--")
print(f"{'x-----33--':->17}--")
print(f"{'x------3--':->17}--")

# ":->" - zelimo da znak '-' ispise na pocetku stringa. 
# 17 - svaki string u ispisu (prvi nacin) ima 17 karaktera. Ovo omogucava da ispis na ovakav nacin bude isti kao 
# sa primjera u postavci zadatka.  