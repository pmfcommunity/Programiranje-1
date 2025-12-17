# Napisati program koji od korisnika zahtijeva unos liste vrijednosti. Vrijednosti se unose u jednom redu razdvojene praznim mjestom. 
# Nakon sto unese listu korisnik unosi vrijednost n u narednom redu. Program treba ispisati razliku izmedju najveceg i n-tog 
# najveceg broja u listi. Mozete pretpostaviti da korisnik nikada nece unijeti n vece od duzine liste. U narednom primjeru
# najveca rijednost u listi je 98, a treca najveca 83, pa je njihova razlika 15.
# 39 98 16 83 78 66 95 13 78
# 3 

brojevi = input()
n = int(input())
brojevi = brojevi.split(" ")

lista_brojeva = []
for broj in brojevi: 
    lista_brojeva.append(int(broj))

najveci = max(lista_brojeva)

for broj in range(n - 1): 
    maksimum = max(lista_brojeva)
    lista_brojeva.remove(maksimum)

n_ti_najveci = max(lista_brojeva)

print(najveci - n_ti_najveci)