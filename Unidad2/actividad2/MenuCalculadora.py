# Con esta función realizamos la SUMA de dos numero proporcionados por parametros
def sum(a, b):
    return a + b;

# Con esta función realizamos la RESTA de dos numero proporcionados por parametros
def subt(a, b):
    return a - b;

# Con esta función realizamos la MULTIPLICACION de dos numero proporcionados por parametros
def mult(a, b):
    return a * b;

# Con esta función realizamos la DIVISION de dos numero proporcionados por parametros
def divi(a, b):
    if b == 0:
        return 'Error, La división entre 0 no es posible!'
    else:
        return a / b;
    
# Con esta función realizamos la POTENCIA CUADRADA de dos numero proporcionados por parametros
def sqrP(a, b):
    return a ** b;

def default():
    return 'Opcion de calculadora Invalida'

def switch(case, a, b):
    operations = {
        1: sum(a, b),
        2: subt(a, b),
        3: mult(a, b),
        4: divi(a, b),
        5: sqrP(a, b)
    }
    return operations.get(case, default())

def menu():
    print('\nQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
    print('QQQ""""""""""""""""""""""""""QQQ')
    print('QQQ""""""""""""""""""""""""""QQQ')
    print('QQQ""""""""""""""""""""""""""QQQ')
    print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
    print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
    print('QQQ""""""""""""""""""""""""""QQQ')
    print('QQQ""""""""""""""""""""""""""QQQ')
    print('QQQ"""QQQQQ""QQQQQ"""QQQQQ"""QQQ')
    print('QQQ"""QQQQQ""QQQQQ"""QQQQQ"""QQQ')
    print('QQQ""""""""""""""""""""""""""QQQ')
    print('QQQ"""QQQQQ""QQQQQ"""QQQQQ"""QQQ')
    print('QQQ"""QQQQQ""QQQQQ"""QQQQQ"""QQQ')
    print('QQQ""""""""""""""""""""""""""QQQ')
    print('QQQ"""QQQQQ""QQQQQ"""QQQQQ"""QQQ')
    print('QQQ"""QQQQQ""QQQQQ"""QQQQQ"""QQQ')
    print('QQQ""""""""""""""""""""""""""QQQ')
    print('QQQ""""QQQQQQQQQQQQQQQQQQQ"""QQQ')
    print('QQQ""""QQQQQQQQQQQQQQQQQQQ"""QQQ')
    print('QQQ""""""""""""""""""""""""""QQQ')
    print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
    print('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ\n')
    
    print("----------- Calculadora -----------")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia Cuadrada")
    print("-----------------------------------")
    
menu()
case = int(input("Seleccione una opcion: "))

a = int(input("\nValor de a: "))
b = int(input("Valor de b: "))

print(f'\nRespuesta: {switch(case, a, b)}')