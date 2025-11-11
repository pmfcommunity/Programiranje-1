n = int(input())

for i in range(1, n + 1): 
    broj_djelilaca = 0 
    for j in range(1, i + 1): 
        if i % j == 0: broj_djelilaca += 1 
    print(f"{i}: {broj_djelilaca}")