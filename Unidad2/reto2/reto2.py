import os

# Funcion para imprimir menu
def printMenu ():
        os.system("cls")
        print('MENU DE OPCIONES\n') 
        for menuOption in menuOptions:
            print(f'{menuOptions.index(menuOption) + 1}. {menuOption}')

print('Bienvenido al sistema de ubicación para zonas públicas WIFI');

# Se solicitan las credeciales de acceso como userName y Password
userName = input('Nombre de Usuario: ');
if userName != "51676":
    print('Error');
else:
    password = input('Contraseña: ');
    if password != '67615':
        print('Error');
    # Una vez validadas las credenciales, se procese a realizar un captcha de seguridad
    else:
        # Filtramos los ultimos 3 digitos del usuario ingresado
        firstTerm = int(password[0:3]);
        secondTerm = (5%6) + (5%6) - (5-(1+1));
        captcha = int(input('Valor Captcha {} + {}: '.format(firstTerm, secondTerm)));
        if captcha != firstTerm + secondTerm:
            print('Error');
        else:
            print('Sesión Iniciada'); 
            os.system("cls")
            
            menuOptions = ['Cambiar contraseña', 'Ingresar coordenadas actuales', 'Ubicar zona wifi más cercana', 'Guardar archivo con ubicación cercana', 'Actualizar registros de zonas wifi desde archivo', 'Elegir opción de menú favorita', 'Cerrar sesión.'];   
            
            #controlMenu es la variable de control para el menu, mientras su valor sea menor o igual a 3, el usuario tendra la posibilidad para navegar por el menu. De sobrepasar este valor, se terminara la ejecucion del programa
            
            controlMenu = 1
            
            # Se imprime el menu inicial sin cambios
            printMenu();
            
            while controlMenu <= 3:        
                
                chosenMenuOption = int(input('\nElija una opción: '));
                
                if chosenMenuOption == 6:
                    # Se reinicia controlMenu a 1 que a los 3 errores SEGUIDOS imprima error y finalice el programa
                    controlMenu = 1;
                    
                    favoriteMenuOption = int(input('\nSeleccione opción favorita: '))
                    
                    if favoriteMenuOption < 1 or favoriteMenuOption > 5:
                        print('\nError')
                        exit()
                    else:
                        os.system('cls')
                        print('Adivinanzas para confirmación de Usuario\n')                        
                        print('Primera Adivinanza:')
                        print('Si quieres saber quién soy, espera a que llueva. Contando los colores del arcoíris tendrás la prueba.')
                        firstRiddle = int(input('\nRespuesta: '))
                        
                        if firstRiddle != 7:
                            print('Error')
                            printMenu()
                        else:  
                            print('\nSegunda Adivinanza:')
                            print('Si le sumas su hermano gemelo al tres, ya sabes cuál es!')
                            secondRiddle = int(input('\nRespuesta: '))
                            
                            if secondRiddle != 6:
                                print('Error')
                                printMenu()
                            else:                                                   
                                chosenMenuBackup = menuOptions[favoriteMenuOption - 1]
                                menuOptions.remove(menuOptions[favoriteMenuOption - 1])
                                menuOptions.insert(0, chosenMenuBackup)
                                printMenu()
                else:                
                    if chosenMenuOption < 1 or chosenMenuOption > 7:  
                        controlMenu = controlMenu + 1 
                        print('Error\n')
                    else:
                        controlMenu = 1;
                        if chosenMenuOption == 7:                 
                            print('\nHasta pronto')
                            exit()                        
                        else:
                            print('\nUsted ha elegido la opción {}'.format(chosenMenuOption))
                            exit()