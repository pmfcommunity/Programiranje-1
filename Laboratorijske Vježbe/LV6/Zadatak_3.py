# Napisati program kojim se unosi n brojeva u listu. Program ispisuje samo razlicite elemente liste. Na primjer, za unos 
# 1, 10, 5, 10, 2, 1, 3 program ispisuje 1, 10, 5, 2, 3

n = int(input())

lista_brojeva = []
for _ in range(n): 
    broj = int(input())
    if broj not in lista_brojeva: 
        lista_brojeva.append(broj)
        
for broj in lista_brojeva: 
    print(broj, end=" ")
print()