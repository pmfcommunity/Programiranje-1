# Napisati program koji pronalazi i ispisuje tri broja koja ispunjavaju naredne uslove:
# - Sva tri broja su palindromi (brojevi koji se citaju jednako sa lijeva na desno i sa desna na lijevo)
# - Prvi broj je dvocifren
# - Drugi broj je trocifren
# - Treci broj je cetverocifren i zbir je prva dva broja

for prvi in range(10, 100): 
    for drugi in range(100, 1000):
            treci = prvi + drugi 
            jesu_li_svi_palindrom = False 
            jel_prvi_dvocifren = False 
            jel_drugi_trocifren = False 
            jel_treci_cetverocifren_i_zbir_prva_dva = False 

            prvi_string = str(prvi)
            drugi_string = str(drugi)
            treci_string = str(treci)

            if prvi_string == prvi_string[::-1] and drugi_string == drugi_string[::-1] and treci_string == treci_string[::-1]: 
                jesu_li_svi_palindrom = True

            if prvi >= 10 and prvi <= 99: jel_prvi_dvocifren = True
            if drugi >= 100 and drugi <= 999: jel_drugi_trocifren = True 
            if treci >= 1000 and treci <= 9999: 
                if treci == prvi + drugi: jel_treci_cetverocifren_i_zbir_prva_dva = True 

            if jesu_li_svi_palindrom and jel_prvi_dvocifren and jel_drugi_trocifren and jel_treci_cetverocifren_i_zbir_prva_dva: 
                print(prvi, drugi, treci)