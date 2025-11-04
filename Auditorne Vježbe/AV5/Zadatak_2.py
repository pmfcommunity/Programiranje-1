# Napisati program koji ispisuje prvih n prirodnih brojeva,
# po jedan u svakom redu. Brojevi idu formatirani naizmjenicno
# na lijevu pa na desnu stranu. 

n = int(input())

for i in range(1, n + 1): 
    for j in range(1, n + 1): 
        if i % 2 == 0: 
            if j == 1:
                print(i, end=" ")
            else: print(" ", end=" ")
        if i % 2 != 0:
            if j == n: 
                print(i, end=" ")
            else: print(" ", end=" ")
    print()