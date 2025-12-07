# Napisati program koji ispisuje sve permutacije neke liste. Na primjer, za listu [1, 2, 3] ispisuju se permutacije:
# [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]

def permutacije(brojevi): 
    for i in range(len(brojevi)):
        for j in range(len(brojevi)):
            for k in range(len(brojevi)): 
                if i != j and i != k and k != j:
                    print(brojevi[i], brojevi[j], brojevi[k])
permutacije([1, 2, 3])