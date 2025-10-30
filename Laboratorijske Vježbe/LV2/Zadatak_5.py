# Napisati program koji trazi da se unese sa tastature koefcijenti sistema jednacina:
# a1 * x + b1 * y + c1 = 0
# a2 * x + b2 * y + c2 = 0

a1 = float(input("Unos koefcijenta a1: "))
b1 = float(input("Unos koefcijenta b1: "))
c1 = float(input("Unos koefcijenta c1: "))

a2 = float(input("Unos koefcijenta a2: "))
b2 = float(input("Unos koefcijenta b2: "))
c2 = float(input("Unos koefcijenta a2: "))

D = a1 * b2 - a2 * b1

if D != 0:
    x = (b1*c2 - b2*c1) / D
    y = (c1*a2 - c2*a1) / D
print(f"x: {x}, y: {y}")