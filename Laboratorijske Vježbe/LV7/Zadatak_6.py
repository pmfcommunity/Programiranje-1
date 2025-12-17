# Napisati program kojim se unosi n rijeci u listu. Sve rijeci moraji biti razlicite. Ukoliko se neka ponovi, u smislu da je 
# prethodno unesena, trazi se ponovni unos te rijeci. 
# Program potom izbacuje iz liste sve rijeci cija je duzina veca od 5. 

n = int(input())

lista_rijeci = []
i = 0
while i < n: 
    rijec = input()
    if rijec not in lista_rijeci: 
        lista_rijeci.append(rijec)
        i += 1 
    else: 
        print(f"Rijec {rijec} vec unesena!")

nova_lista = []
for rijec in lista_rijeci: 
    if len(rijec) > 5: 
        continue 
    else: 
        nova_lista.append(rijec)

print(nova_lista)