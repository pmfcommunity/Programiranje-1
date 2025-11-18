# Napisati program kojim se unosi n cijelih brojeva. Program ispisuje srednji broj po veličini.

n = int(input())

brojevi = []
for i in range(n): 
    x = int(input())
    brojevi.append(x)

sredina = len(brojevi) // 2 
brojevi.sort()

prvi_dio = brojevi[:sredina]
drugi_dio = brojevi[sredina:]

prvi_dio_max = max(prvi_dio)
drugi_dio_min = min(drugi_dio)

print(max(prvi_dio_max, drugi_dio_min))

# ili smo samo mogli (nakon unosa liste)
# brojevi.sort()
# print(brojevi[n // 2])