import os
import sys
import math

# Credenciales
user = 51676
passwordKey = 67615

# Declaración listas
coordinateMatrix = []
# Funcion para imprimir menu
def printmenu():
    os.system("cls")
    print('MENU DE OPCIONES\n') 
    for menuOption in menuOptions:
        print(f'{menuOptions.index(menuOption) + 1}. {menuOption}')

# Cambiar de password
def changePassword():
    
    checkPassword = int(input('\nIngrese contraseña actual: '))
    global passwordKey
    if checkPassword != passwordKey:
        print('Error')
        sys.exit()
    else:
        newPassword = 0
        while newPassword == 0:
            newPassword = int(input('Ingrese nueva contraseña: '))            
            if newPassword == passwordKey:
                print('\nLa nueva contraseña no puede ser igual a la contraseña actual.\n')
                newPassword = 0;
            else:
                passwordKey = newPassword
        newPassword = 0
        printmenu()
        return passwordKey

# Solicitar coordenadas por primera vez
def coordinates():
    global coordinateMatrix
    for i in range(0, 3):
        print('Latitud y Longitud para {}:'.format(coordinatePlaces[i]))
        latitude = input('\nIngresar coordenada de Latitud entre limite inferior de 1.740 y limite superior de 1.998: ')
        if latitude == '':
            print('Error')
            sys.exit()
        elif float(latitude) < 1.740 or float(latitude) > 1.998:
            print('Error coordenada')
            sys.exit()
        else:
            length = input('Ingresar coordenada de Longitud entre limite oriental de -75.689 y limite occidental de -75.950: ')
            if length == '':
                print('Error')
                sys.exit()
            elif float(length) > -75.689 or float(length) < -75.950:
                print('Error coordenada')
                sys.exit()
            else:
                print('')
                coordinateMatrix.append([latitude, length])

# Agregar nuevas coordenadas 
def newCoordenate():
    global chosenUpdateOption
    global coordinateMatrix
    coordinateMatrix.pop(chosenUpdateOption - 1)
    print(coordinateMatrix)
    latitude = input('\nIngresar coordenada de Latitud entre limite inferior de 1.740 y limite superior de 1.998: ')
    if latitude == '':
        print('Error')
        sys.exit()
    elif float(latitude) < 1.740 or float(latitude) > 1.998:
        print('Error actualización')
        sys.exit()
    else:
        length = input('Ingresar coordenada de Longitud entre  limite oriental de -75.689 y limite occidental de -75.950: ')
        if length == '':
            print('Error')
            sys.exit()
        elif float(length) > -75.689 or float(length) < -75.950:
            print('Error actualización')
            sys.exit()
        else:
            newCoordenate = [latitude, length]
            coordinateMatrix.insert(chosenUpdateOption - 1, newCoordenate)

# Calcular distancia
def distanceCal(lat1, lon1, lat2, lon2):
    R = 6372.795477598
    term1 = pow(math.sin((lat2 - lat1)/2), 2)
    term2 = math.cos(lat1)
    term3 = math.cos(lat2)
    term4 = pow(math.sin((lon2 - lon1)/2), 2)
    raiz = math.sqrt(term1 +  term2 * term3 * term4)
    distance = round(2 * R * math.asin(raiz), 0)
    return distance

def truncate(num, n):
    integer = int(num * (10**n))/(10**n)
    return float(integer)

def timeToWifiZone(distanceZoneWifi, vehicle): 
    time = truncate((distanceZoneWifi / vehicle), 0) 
    return time

def ubicationZoneWifi(chosenMenuDistance):
    os.system('cls')
    latitudInicial = float(coordinateMatrix[chosenMenuDistance - 1][0])
    longitudInicial = float(coordinateMatrix[chosenMenuDistance - 1][1])
    for nearWifi2 in range(0, 4):
        lati2 = float(filteredWifiZones[nearWifi2][0])
        long2 = float(filteredWifiZones[nearWifi2][1])
        distanceWifiZones.append(distanceCal(latitudInicial, longitudInicial, lati2, long2)) 
        
    latitudDestino = truncate(filteredWifiZones[distanceWifiZones.index(min(distanceWifiZones))][0], 3)
    longitudDestino = truncate(filteredWifiZones[distanceWifiZones.index(min(distanceWifiZones))][1], 3)
    metersPrint = round(min(distanceWifiZones))
    activeUsersPrint = filteredWifiZones[distanceWifiZones.index(min(distanceWifiZones))][2]
    
    print('Zonas wifi cercanas con menos usuarios')
    print(f"La zona wifi 1: ubicada en ['{latitudDestino}', '{longitudDestino}'] a {metersPrint} metros, tiene en promedio {activeUsersPrint} usuarios")
    
    distanceWifiZones.remove(min(distanceWifiZones))
    latitudDestino2 = truncate(filteredWifiZones[distanceWifiZones.index(min(distanceWifiZones))][0], 3)
    longitudDestino2 = truncate(filteredWifiZones[distanceWifiZones.index(min(distanceWifiZones))][1], 3)
    metersPrint2 = round(min(distanceWifiZones))
    activeUsersPrint2 = filteredWifiZones[distanceWifiZones.index(min(distanceWifiZones))][2]
    
    print(f"La zona wifi 2: ubicada en ['{latitudDestino2}', '{longitudDestino2}'] a {metersPrint2} metros, tiene en promedio {activeUsersPrint2} usuarios")       
    
    chosenMenuNearWifi = int(input('Elija 1 o 2 para recibir las indicaciones de llegada: '))
    if chosenMenuNearWifi < 1 or chosenMenuNearWifi > 2:
        print('Error zona wifi')
        sys.exit()
    else:
        pie = 0.483
        auto = 20.83
        if longitudInicial < longitudDestino:
            if latitudInicial < latitudDestino:
                print('\nPara llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte')        
            else:
                print('\nPara llegar a la zona wifi dirigirse primero al oriente y luego hacia el sur')        
        else:
            if latitudInicial < latitudDestino:
                print('\nPara llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte')        
            else:
                print('\nPara llegar a la zona wifi dirigirse primero al occidente y luego hacia el sur')    
                
        if chosenMenuNearWifi == 1: 
            print('\nTiempo a pie {} segundos'.format(timeToWifiZone(metersPrint, pie)))
            print('Tiempo en auto {} segundos'.format(timeToWifiZone(metersPrint, auto)))            
        else:
            print('\nTiempo a pie {} segundos'.format(timeToWifiZone(metersPrint2, pie)))
            print('Tiempo en auto {} segundos'.format(timeToWifiZone(metersPrint2, auto)))
        
        exitWifiZones = int(input('\nPresione 0 para salir '))
        
        if exitWifiZones == 0:
            printmenu()
# ================================================================
#                       INICIO PROGRAMA 
            
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
            op7 = 'Cerrar sesión.'
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
                                changePassword()  
                            # Ingresar coordenadas actuales
                            elif menuOptions[chosenMenuOption - 1] == menuOptions[menuOptions.index(op2)]:
                                coordinatePlaces = ['Trabajo', 'Casa', 'Parque']
                                if len(coordinateMatrix) == 0:
                                    os.system('clear')
                                    coordinates()
                                    printmenu()
                                else:
                                    os.system('cls')
                                    maxSouth = [coordinateMatrix[0][0], coordinateMatrix[1][0], coordinateMatrix[2][0]]
                                    maxWest = [coordinateMatrix[0][1], coordinateMatrix[1][1], coordinateMatrix[2][1]]
                                    for i in range(0,len(coordinateMatrix)):
                                        print('Coordenada [Latitud, Longitud] {}: {}'.format(i + 1, coordinateMatrix[i]))
                                    print('La coordenada {} es la que está más al sur'.format(maxSouth.index(min(maxSouth))))
                                    print('La coordenada {} es la que está más al occidente'.format(maxWest.index(min(maxWest))))
                                    print('Presione 1, 2 o 3 para actualizar la respectiva coordenada. ')
                                    chosenUpdateOption = int(input(('Presione 0 para regresar al menu. ')))
                                    if chosenUpdateOption < 0 and chosenUpdateOption > 3:
                                        print('Error')
                                        sys.exit()
                                    elif chosenUpdateOption == 0:
                                        printmenu()
                                    elif chosenUpdateOption == 1 or chosenUpdateOption == 2 or chosenUpdateOption == 3:
                                        newCoordenate()
                                        printmenu()
                                    else:
                                        print('Error actualización')
                                        sys.exit()
                            # Ubicar Zona Wifi mas cercana
                            elif menuOptions[chosenMenuOption - 1] == menuOptions[menuOptions.index(op3)]:
                                if len(coordinateMatrix) == 0:
                                    print('Error sin registro de coordenadas')
                                    sys.exit()
                                else:
                                    os.system('cls')
                                    filteredWifiZones = []
                                    
                                    zonesWifi = [[1.811, -75.820, 58], [1.919, -75.843, 1290], [1.875, -75.877, 110], [1.938, -75.764, 114]]
                                    
                                    for i in range(0, len(zonesWifi)):
                                        if zonesWifi[i][2] == 58 or zonesWifi[i][2] == 1290 or zonesWifi[i][2] == 110 or zonesWifi[i][2] == 114:
                                            if zonesWifi[i][0] > 1.740 and zonesWifi[i][0] < 1.998:
                                                if zonesWifi[i][1] < -75.689 and zonesWifi[i][1] > -75.950:
                                                    filteredWifiZones.append(zonesWifi[i])
                                        
                                    for i in range(0,len(coordinateMatrix)):
                                        print("Coordenada [Latitud, Longitud] {}: ['{}', '{}']".format(i + 1, str(coordinateMatrix[i][0]), str(coordinateMatrix[i][1])))
                                        
                                    chosenMenuDistance = int(input('Por favor elija su ubicación actual (1, 2 ó 3) para calcular la distancia de los puntos de conexión: '))
                                    
                                    if chosenMenuDistance < 1 or chosenMenuDistance > 3:
                                        print('Error ubicación')
                                        sys.exit()
                                    else:
                                        distanceWifiZones = []
                                        ubicationZoneWifi(chosenMenuDistance)
                            else:
                                print('Ud a elegido la opcion {}'.format(chosenMenuOption))
                                sys.exit()