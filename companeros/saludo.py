#saludo de acuerdo a la hora del dia
hora = (int(input("Que hora es? (desde la 1a.m. hasta las 24p.m.):  ")))
if hora>0 and hora<25:
    if hora>=1 and hora<=12:
        print("Buenos dias")
    else:
        if hora==12:
            print("Buenos dias") 
        else:
            if hora>12 and hora<=17:
                print("Buenas tardes")
            else:
                if hora>=18 and hora<=24:
                    print("Buenas noches")
                else:
                    print("Hora errada")
else:
    print ("Hora errada")       