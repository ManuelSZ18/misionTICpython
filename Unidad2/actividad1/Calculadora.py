def sum(a, b):
    return a + b;

def subt(a, b):
    return a - b;

def mult(a, b):
    return a * b;

def divi(a, b):
    if b == 0:
        return 'Error, La división entre 0 no es posible!'
    else:
        return a / b;
    
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
    print("----------- Calculadora -----------")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia Cuadrada")
    print("-----------------------------------")
    
menu()
case = int(input("Seleccione una opcion: "))

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))

print(switch(case, a, b))