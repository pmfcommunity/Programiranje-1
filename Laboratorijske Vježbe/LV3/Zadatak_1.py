# Napisati program koji od korisnika trazi da unese ukupan broj bodova sa vjezbi, parcijalih ispita i 
# zavrsnog ispita. Potom se ispise ocjena iz tog predmeta u odnosu na broj ukupnih bodova.

bodovi_sa_vjezbi = int(input("Unesite bodove sa vjezbi: "))

bodovi_sa_parcijalnih_ispita = int(input("Uneste bodove sa parcijalnih isita: "))

bodovi_sa_zavrsnog_ispita = int(input("Unesite bodove sa zavrsnog ipsita: "))

if bodovi_sa_vjezbi < 0 or bodovi_sa_vjezbi > 20 or \
    bodovi_sa_parcijalnih_ispita < 0 or bodovi_sa_parcijalnih_ispita > 40 or \
        bodovi_sa_zavrsnog_ispita < 0 or bodovi_sa_zavrsnog_ispita > 40:
            print("Uneseni bodovi nisu tacni!")
            print(f"Bodovi sa vjezbi: {bodovi_sa_vjezbi} (0-20)")
            print(f"Bodovi sa parcijalnih ispita: {bodovi_sa_parcijalnih_ispita} (0-40)")
            print(f"Bodovi sa zavrsnog ispita: {bodovi_sa_zavrsnog_ispita} (0-40)")
else:
    ukupan_broj_bodova = bodovi_sa_vjezbi + bodovi_sa_parcijalnih_ispita + bodovi_sa_zavrsnog_ispita

    ocjena = 0
    if ukupan_broj_bodova < 55: ocjena = 5
    elif ukupan_broj_bodova < 65: ocjena = 6
    elif ukupan_broj_bodova < 75: ocjena = 7
    elif ukupan_broj_bodova < 85: ocjena = 8
    elif ukupan_broj_bodova < 95: ocjena = 9 
    else: ocjena = 10 

    print(f"Ukupan broj bodova sa predmeta jeste {ukupan_broj_bodova}, a to znaci da vam je ocjena {ocjena}.") 