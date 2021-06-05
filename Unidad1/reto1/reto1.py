import os
print('Bienvenido al sistema de ubicación para zonas públicas WIFI');
userName = input('Nombre de Usuario: ');
if userName != "51676":
    print('Error');
else:
    password = input('Contraseña: ');
    if password != '67615':
        print('Error');
    else:
        firstTerm = int(password[0:3]);
        secondTerm = (5%6) + (5%6) - (5-(1+1));
        captcha = int(input('Valor Captcha {} + {}: '.format(firstTerm, secondTerm)));
        if captcha != firstTerm + secondTerm:
            print('Error');
        else:
            print('Sesión Iniciada'); 
            os.system("cls")