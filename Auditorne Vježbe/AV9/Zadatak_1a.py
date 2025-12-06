# Napisati funkciju koja vraca apsolutnu vrijednost broja. 

def apsolutna(x):
    if x > 0: return x 
    else: return -x

a = int(input())
print(apsolutna(a))