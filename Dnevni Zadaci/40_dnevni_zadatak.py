# Napisati program koji za proslijedjeni broj n ispisuje naziv kolone u Excel-u. Broj 1 predstavlja kolonu A, 2 je B, 3 je C, 
# 26 je Z, 27 je 27, 28 je AB, dok je 701 npr. ZY.

def excel_kolona(n):
    
    if n <= 0:
        return ""
    
    rezultat = ""
    
    while n > 0:
        ostatak = n % 26

        if ostatak == 0:

            ostatak = 26
            n = (n // 26) - 1
        else:
            n = n // 26
            
        karakter = chr(ord('A') + ostatak - 1)
        
        rezultat = karakter + rezultat
        
    return rezultat

print(f"1 -> {excel_kolona(1)}")    
print(f"26 -> {excel_kolona(26)}")  
print(f"27 -> {excel_kolona(27)}")  
print(f"28 -> {excel_kolona(28)}")  
print(f"702 -> {excel_kolona(702)}") 
print(f"701 -> {excel_kolona(701)}") 