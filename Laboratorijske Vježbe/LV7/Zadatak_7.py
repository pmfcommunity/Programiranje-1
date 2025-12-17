# Napisati program kojim se unosi n i potom n floating point brojeva. Program ispisuje broj pojavlijvanja najveceg elementa u nizu. 

n = int(input())
lista_brojeva = []

for _ in range(n): 
    lista_brojeva.append(int(input()))
for _ in range(n): 
    lista_brojeva.append(float(input()))
    
najveci = max(lista_brojeva)
brojac = 0 

for broj in lista_brojeva: 
    if broj == najveci: brojac += 1 

print(brojac)