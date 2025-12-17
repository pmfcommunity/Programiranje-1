# Napisati funkciju koja za argument prihvata listu stringova. Funkcija vraca broj pojavljivanja najduzeg stringa u listi

def pojavljivanje_najveceg_stringa(recenica): 
    najduza = ""
    for rijec in recenica: 
        if len(rijec) > len(najduza): 
            najduza = rijec 
    
    brojac = 0
    for rijec in recenica: 
        if rijec == najduza: brojac += 1
    return brojac 
    
string = input()
string = string.split(" ")

print(pojavljivanje_najveceg_stringa(string))