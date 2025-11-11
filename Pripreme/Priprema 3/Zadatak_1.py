sati = int(input())
minute = int(input())
sekunde = int(input())
vrijeme = input()

if sati == 12:
    sati = 0

if vrijeme.upper() == "PM":
    sati += 12
print(f"{sati:02}:{minute:02}:{sekunde:02}")