# Napisati program koji unosi e-mail adresu. Smatra se da je e-mail adresa ispravna ako sadrži znak @ , 
# ako je ime (do znaka @  duže od tri karaktera, a dio e-maila iza @ (domena) sadrži barem jednu tačku. 
# Ako je e-mail adresa ispravna (npr. aleksandar.bs@pmf.unsa.ba), program treba da ispiše u obliku 
# ale*****@pmf*****  (po tri prva znaka prije i poslije znaka @).
# Dodatni uslov: dodatno provjeriti da je oznaka zemlje ba, com ili net. 
# U suprotnom smatrati da je e-mail nevalidan.

email = input("Unesite e-mail adresu: ")

email_u_dijelovima = email.split('@')
prije_at = email_u_dijelovima[0]
nakon_at = email_u_dijelovima[1]

if "@" in email and len(prije_at) > 3 and "." in nakon_at and \
    "ba" in nakon_at or "com" in nakon_at or "net" in nakon_at:
        prije_at = prije_at[:3] + "******"
        nakon_at = nakon_at[:3] + "******"
        hidden_email = prije_at + "@" + nakon_at
        print(hidden_email) 
else: print(f"{email} nije ispravna email adresa!")