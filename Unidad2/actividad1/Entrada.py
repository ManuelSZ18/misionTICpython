entero = int(input('Ingrese un numero entero: '));
flotante = float(input('Ingrese un numero flotante: '));
booleano = bool(input('Ingrese un numero booleano: '));
cadena = str(input('Ingrese un numero cadena: '));
tiposDeDatos = [entero, flotante, booleano, cadena]
print(' ')
for dato in tiposDeDatos:
    print('El dato {} es de tipo: {}'.format(dato, type(dato)))