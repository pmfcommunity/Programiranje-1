# Napisati program koji od korisnika trazi da unese cjelobrojne vrijednosti a i b. Program ispisuje i racuna
# povrsinu i obim pravougaonika sa stranicama a i b.

a = int(input("Unesite stranicu a: "))
b = int(input("Unesite stranicu b: "))

povrsina = a * b
obim = 2 * (a + b)
print(f"Povrsina pravougaonika iznosi: {povrsina}\nObim pravougaonika iznosi: {obim}")