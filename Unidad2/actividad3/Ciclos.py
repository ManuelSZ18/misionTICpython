import os
optionsMenu = {0 : 'Salir', 1 : 'Saludar', 2 : 'Es Par', 3 : 'Promedio', 4 : 'Modulo' , 5 : 'Porcentaje', 6 : 'Potencia'};

def menu ():
    print('\nMENU DE OPCIONES\n');
    for option in range(1, len(optionsMenu)):  
        index = option;
        print('{}. {}'.format(index, optionsMenu[index]));
        index = index + 1;
    print('0. {}'.format(optionsMenu[0]));
    
menu()

sentinel = int;

while sentinel != 0 or sentinel != 1 or sentinel != 2 or sentinel != 3 or sentinel != 4 or sentinel != 5:
    sentinel = int((input('\nIngrese opcion de operacion: ')));
    
    if sentinel == 0:
        break
    
    if sentinel == 1:
        
        os.system('clear')
        print('\nOPCION ELEGIDA: SALUDAR!');        
        hour = int(input('\nIngrese una hora del dia en formato 24 horas: '));
        if hour >= 1 and hour < 12:
            print('\nSon las {} a.m. - Buenos dias!'.format(hour));
        elif hour >= 12 and hour < 18:
            print('\nSon las {} p.m. - Buenas tardes!'.format(hour));
        elif hour > 17 and hour < 25:
            print('\nSon las {} p.m. - Buenas Noches!'.format(hour));
        else:
            print('\nLa hora ingresada no es valida!');
        break
    
    if sentinel == 2:
        
        os.system('clear')
        print('\nOPCION ELEGIDA: ES PAR!');        
        number = int(input('\nIngrese numero: '));
        if number % 2 == 0:
            print(f'\n{number} es par!');
        else:
            print(f'\n{number} no es par!');
        break
    
    if sentinel == 3:
        
        os.system('clear')
        print('\nOPCION ELEGIDA: PROMEDIO!\n');        
        number1 = int(input('Ingrese Primer numero: '));
        number2 = int(input('Ingrese Segundo numero: '));
        number3 = int(input('Ingrese Tercer numero: '));
        number4 = int(input('Ingrese Cuarto numero: '));
        number5 = int(input('Ingrese Quinto numero: '));        
        average = (number1 + number2 + number3 + number4 + number5) / 5        
        print(f'\nPromedio : {average}');
        break
    
    if sentinel == 4:
        
        os.system('clear')
        print('\nOPCION ELEGIDA: MODULO!\n'); 
        firstNumber = int(input('Primer Numero: '))
        secondNumber = int(input('Segundo Numero: '));
        module = firstNumber // secondNumber;
        print('\nEl resultado de {} modulo {} es: {}'.format(firstNumber, secondNumber, module))
        break
        
    if sentinel == 5:
        
        os.system('clear')
        print('\nOPCION ELEGIDA: PORCENTAJE!\n');
        print('Calcular el porcentaje de una cantidad dada.\n')    
        amount = int(input('Cantidad: '))
        porcentage = int(input('Porcentaje: '));
        total = (amount*porcentage)/100
        print('\nEl {}% de {} es: {}'.format(porcentage, amount, total))
        break
    
    if sentinel == 6:
        
        os.system('clear')
        print('\nOPCION ELEGIDA: POTENCIA!\n');        
        base = int(input('Base: '))
        exponent = int(input('Exponente: '));
        result = base**exponent
        print('\nEl resultado es: {}'.format(result))
        break