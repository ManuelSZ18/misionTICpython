#RF01
print('Bienvenido al sistema de ubicación para zonas públicas WIFI');
#RF02
userName = input('Nombre de Usuario: ');
if userName != "51676": 
    print('Error');
else:
    password = input('Contraseña: ');
    if password != "67615":
        print('Error');
    else:
        #RF03
        inverseUserName = userName[::-1];
        firstTerm = int(inverseUserName[0:3]);
        secondTerm = (5%6) + (9%6) - 1;
        captcha = int(input('Valor Captcha {} + {}: '.format(firstTerm, secondTerm)));
        if captcha != firstTerm + secondTerm:
            print('Error');
        else:
            #RF04
            print('Sesión iniciada');