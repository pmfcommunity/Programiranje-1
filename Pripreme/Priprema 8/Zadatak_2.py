# Prilikom pisanja Word dokumenta, ukoliko je spellchecker postavljen na engleski jezik,
# svako zasebno malo slovo "i" ce biti zamijenjeno velikim slovom "I". Napisati program u 
# koji korisik unosi tekst, a program ispisuje tekst u kojem je svako zasebno slovo "i" veliko. 
# Program u narednom redu treba oznaciti lokacije na kojima je napravio izmjene koristeci povlaku.

recenica = input() 
nova_recenica = " " + recenica + " "

ispis = ""
ispis_lokacija = ""
for i in range(len(nova_recenica)): 
    if nova_recenica[i] == "i" and nova_recenica[i - 1] == " " and nova_recenica[i + 1] == " ": 
        ispis += "I"
        ispis_lokacija += "-"
    else: 
        ispis += nova_recenica[i]
        ispis_lokacija += " "

print(ispis)
print(ispis_lokacija)