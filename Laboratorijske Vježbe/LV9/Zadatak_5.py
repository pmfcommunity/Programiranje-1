# Matrice mnozimo relativno jednostavno. Ako su nam date dvije matrice A i B formata m x n (m redova i n kolona) i n x k (n redova i k
# kolona), tada je matrica AB formata m x k. Napraviti funkciju koja za date matrice A i B vraca njihov proizvod. Podrazumijeva se da su
# proslijednjene matrice odgovarujec formata 

def proizvod_matrice(a, b): 
    m = len(a)
    n = len(a[0])
    k = len(b[0])
    
    ab = [[0 for _ in range(k)] for _ in range(m)]
    
    for i in range(m):
        for j in range(k):
            for p in range(n): 
                ab[i][j] += a[i][p] * b[p][j]

    return ab 

m = int(input())
n = int(input())
k = int(input())

A = []
B = []

for i in range(m):
    red = []
    for j in range(n): 
        red.append(int(input()))
    A.append(red)

print()

for i in range(n):
    red = []
    for j in range(k): 
        red.append(int(input()))
    B.append(red)

rezultat = proizvod_matrice(A, B)

for red in rezultat: 
    print(red)