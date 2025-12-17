# Napisati funkciju koja racuna faktorijel unesenog broja n i demonstrirati upotrebu funkciju u kratkom programu 


def faktorijel(n):
    proizvod = 1
    for i in range(1, n + 1): 
        proizvod *= i 
    return proizvod 

for i in range(1, 11):
    print(faktorijel(i))         