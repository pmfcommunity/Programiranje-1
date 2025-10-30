# Napisati program koji od korisnika trazi da unese broj osoba zenskog i broj osoba muskog spola u razredu.
# program ispisuje procenat djevojaka i muskaraca od ukupnog broja ucenika u razredu. Procenat se ispisuje na 
# dvije decimale. 

broj_zenskog_spola = int(input("Unesite broj zenskih osoba: "))
broj_muskog_spola = int(input("Unesite broj muskih osoba: "))

ukupan_broj_osoba_u_razredu = broj_zenskog_spola + broj_muskog_spola

procenat_djevojaka = (broj_zenskog_spola / ukupan_broj_osoba_u_razredu) * 100 
procenat_muskaraca = (broj_muskog_spola / ukupan_broj_osoba_u_razredu) * 100 

print(f"Ukupan broj ucenika u razredu je: {ukupan_broj_osoba_u_razredu}, sacinjenih od {round(procenat_djevojaka, 2)}% djevojaka, i {round(procenat_muskaraca, 2)}% muskaraca.")
