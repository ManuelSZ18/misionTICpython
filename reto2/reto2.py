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

opt1 = 'menu1';
opt2 = 'menu2';
opt3 = 'menu3';
opt4 = 'menu4';
opt5 = 'menu5';

menu = [opt1, opt2, opt3, opt4, opt5];

for item in menu:
    index = menu.index(item) + 1;
    print('{}. {}'.format(index, item));
    index = index + 1;
    
favorita = int(input('Ingrese menu favorito: '))
os.system('cls');

menu.insert(0, menu[favorita - 1])
print(menu)

