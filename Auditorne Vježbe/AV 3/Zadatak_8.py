# Napisati program koji pretvara broj godina psa u ekvivalentni ljudski broj godina. Prva godina starosti psa 
# je ekvivalentna 15 ljudskih  godina, dok je druga godina ekvivalentna 9 ljudskih godina. Poslije toga 
# svaka godina starosti psa je ekvivalentna pet godina starosti ljudi.

starosti_psa = int(input("Unesite broj godina psa: "))

ljudske_godine = 0
if starosti_psa == 1:
    ljudske_godine = 15
if starosti_psa == 2:
    ljudske_godine = 15 + 9
if starosti_psa >= 3:
    ljudske_godine = (15 + 9) + (starosti_psa - 2) * 5

print(f"Broj godina psa {starosti_psa} je ekvivalentno {ljudske_godine} ljudskih godina.")