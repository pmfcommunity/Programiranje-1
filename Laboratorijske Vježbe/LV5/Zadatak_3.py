# Napisati program koji za uneseno n ispisuje sve trojke (x, y, z) iz N, x, y, z <= n, takve da vrijedi x^2 + y^2 = z^2

n = int(input())

for x in range(1, n + 1):
    for y in range(x, n + 1):
        for z in range(y, n + 1): 
            if x ** 2 + y ** 2 == z ** 2:
                print(x, y, z)