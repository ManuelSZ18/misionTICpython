import os

entero = int(input('Ingrese un numero entero: '));
flotante = float(input('Ingrese un numero flotante: '));
booleano = bool(input('Ingrese un numero booleano: '));
cadena = str(input('Ingrese un numero cadena: '));

tiposDeDatos = [entero, flotante, booleano, cadena]

os.system('cls')
os.system('clear')

for dato in tiposDeDatos:
    print('El dato {} es de tipo: {}'.format(dato, type(dato)))
