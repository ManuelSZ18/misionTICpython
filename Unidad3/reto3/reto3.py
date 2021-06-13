import os
import sys
import numpy as np
# Funcion para imprimir menu
def printmenu():
    os.system("cls")
    print('MENU DE OPCIONES\n') 
    for menuOption in menuOptions:
        print(f'{menuOptions.index(menuOption) + 1}. {menuOption}')

# Credenciales
user = 51676
passwordKey = 67615

print('Bienvenido al sistema de ubicación para zonas públicas WIFI')

# Se solicitan las credeciales de acceso como userName y Password
userName = int(input('Nombre de Usuario: '))
if userName != user:
    print('Error')
else:
    passwordInput = int(input('Contraseña: '))
    if passwordInput != passwordKey:
        print('Error')
    # Una vez validadas las credenciales, se procese a realizar un captcha de seguridad
    else:
        # Filtramos los ultimos 3 digitos del usuario ingresado
        numberCaptcha = str(passwordInput)
        firstTerm = int(numberCaptcha[0:3])
        secondTerm = (5%6) + (5%6) - (5-(1+1))
        captcha = int(input('Valor Captcha {} + {}: '.format(firstTerm, secondTerm)))
        if captcha != firstTerm + secondTerm:
            print('Error')
        else:
            print('Sesión Iniciada')
            os.system("cls")
            op1 = 'Cambiar contraseña'
            op2 = 'Ingresar coordenadas actuales'
            op3 = 'Ubicar zona wifi más cercana'
            op4 = 'Guardar archivo con ubicación cercana'
            op5 = 'Actualizar registros de zonas wifi desde archivo'
            op6 = 'Elegir opción de menú favorita'
            op7= 'Cerrar sesión.'
            menuOptions = [op1, op2, op3, op4, op5, op6, op7]
            
            #controlMenu es la variable de control para el menu, mientras su valor sea menor o igual a 3, el usuario tendra la posibilidad para navegar por el menu. De sobrepasar este valor, se terminara la ejecucion del programa
            
            controlMenu = 1
            
            # Se imprime el menu inicial sin cambios
            printmenu()
            
            while controlMenu <= 3:        
                
                chosenMenuOption = int(input('\nElija una opción: '))
                
                if chosenMenuOption == 6:
                    # Se reinicia controlMenu a 1 que a los 3 errores SEGUIDOS imprima error y finalice el programa
                    controlMenu = 1
                    
                    favoriteMenuOption = int(input('\nSeleccione opción favorita: '))
                    
                    if favoriteMenuOption < 1 or favoriteMenuOption > 5:
                        print('\nError')
                        break
                    else:
                        os.system('cls')
                        print('Adivinanzas para confirmación de Usuario\n')                        
                        print('Primera Adivinanza:')
                        print('Si quieres saber quién soy, espera a que llueva. Contando los colores del arcoíris tendrás la prueba.')
                        firstRiddle = int(input('\nRespuesta: '))
                        
                        if firstRiddle != 7:
                            print('Error')
                            printmenu()
                        else:  
                            print('\nSegunda Adivinanza:')
                            print('Si le sumas su hermano gemelo al tres, ya sabes cuál es!')
                            secondRiddle = int(input('\nRespuesta: '))
                            
                            if secondRiddle != 6:
                                print('Error')
                                printmenu()
                            else:                                                   
                                chosenMenuBackup = menuOptions[favoriteMenuOption - 1]
                                menuOptions.remove(menuOptions[favoriteMenuOption - 1])
                                menuOptions.insert(0, chosenMenuBackup)
                                printmenu()
                else:                
                    if chosenMenuOption < 1 or chosenMenuOption > 7:  
                        controlMenu = controlMenu + 1 
                        print('Error\n')
                    else:
                        controlMenu = 1
                        if chosenMenuOption == 7:                 
                            print('\nHasta pronto')
                            break                        
                        else:
                            # Cambio de Contraseña
                            if menuOptions[chosenMenuOption - 1] == menuOptions[menuOptions.index(op1)]:
                                whileControl = False
                                while whileControl == False:  
                                        confirmation = int(input('\nIngrese contraseña actual: '))
                                        if confirmation != passwordKey:
                                            print('Error')
                                            sys.exit()
                                        else:
                                            whileControl = True
                                            newPassword = int(input('\nIngrese la nueva constraseña: '))                                    
                                            if newPassword == passwordKey:
                                                print('La nueva contraseña no puede ser igual a la contraseña actual\n')
                                            else:
                                                passwordKey  = newPassword   
                                                printmenu()
                            # Ingresar coordenadas actuales
                            elif menuOptions[chosenMenuOption - 1] == menuOptions[menuOptions.index(op2)]:
                                    latitude = input('Ingresar coordenada de Latitud: ')
                                    if latitude == '':
                                        print('Error')
                                        sys.exit()
                                    elif float(latitude) < 1.740 or float(latitude) > 1.998:
                                        print('Error coordenada')
                                        sys.exit()
                                    else:
                                        length = input('Ingresar coordenada de Longitud: ')
                                        if length == '':
                                            print('Error')
                                            sys.exit()
                                        elif float(length) > -75.950 or float(length) < -75.689:
                                            print('Error coordenada')
                                            sys.exit()
                                        else:
                                            coordinateMatrix = np.array([[latitude, length]])
                                            control = 0
                                            while control < 2:
                                                latitude = input('Ingresar coordenada de Latitud: ')
                                                if latitude == '':
                                                    print('Error')
                                                    sys.exit()
                                                elif float(latitude) < 1.740 or float(latitude) > 1.998:
                                                    print('Error coordenada')
                                                    sys.exit()
                                                else:
                                                    length = input('Ingresar coordenada de Longitud: ')
                                                    if length == '':
                                                        print('Error')
                                                        sys.exit()
                                                    elif float(length) > -75.950 or float(length) < -75.689:
                                                        print('Error coordenada')
                                                        sys.exit()   
                                                    else:                                            
                                                        coordinateMatrix = np.append(coordinateMatrix, [[latitude, length]], axis = 0)
                                                        control = control + 1
                                            print(coordinateMatrix)  
                                            sys.exit()
                            else:
                                print('Ud a elegido la opcion {}'.format(chosenMenuOption))
                                sys.exit()