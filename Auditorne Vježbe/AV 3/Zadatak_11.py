# Horizontalne i vertikalne linije sahovske ploce oznacene su brojevima 1 do 8. Unosimo cetiri prirodna broja 
# a, b, c, i d. Program odreduje da li su polja (a, b) i (c, d) iste boje ili ne. Prva koordinata uredjenog 
# para oznacava broj reda, a druga broj kolone u kojoj se polje nalazi. 

print("Unesite koordinate a i b:")
a = int(input())
b = int(input())

print("Unesite koordinate c i b:")
c = int(input())
d = int(input())

koordinate_boja_1 = ""
koordinate_boja_2 = "" 

if a % 2 == 0 and b % 2 == 0:
    koordinate_boja_1 = "bijela"
if a % 2 != 0 and b % 2 != 0:
    koordinate_boja_1 = "bijela"
if a % 2 == 0 and b % 2 != 0:
    koordinate_boja_1 = "crna"
if a % 2 != 0 and b % 2 == 0:
    koordinate_boja_1 = "crna"
    
if c % 2 == 0 and d % 2 == 0:
    koordinate_boja_2 = "bijela"
if c % 2 != 0 and d % 2 != 0:
    koordinate_boja_2 = "bijela"
if c % 2 == 0 and d % 2 != 0:
    koordinate_boja_2 = "crna"
if c % 2 != 0 and d % 2 == 0:
    koordinate_boja_2 = "crna"
    
if koordinate_boja_1 == koordinate_boja_2:
    print(f"Koordinate ({a}, {b}) i ({c}, {d}) su iste boje:")
    print(f"({a},{b}): {koordinate_boja_1}\n({c},{d}): {koordinate_boja_2}")
else: 
    print(f"Koordinate ({a}, {b}) i ({c}, {d}) nisu iste boje:")
    print(f"({a},{b}): {koordinate_boja_1}\n({c},{d}): {koordinate_boja_2}")