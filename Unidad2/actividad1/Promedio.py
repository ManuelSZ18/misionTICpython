import statistics
print('Para calcular el promedio:')
num1 = int(input('Ingrese primer número: '));
num2 = int(input('Ingrese segundo número: '));
num3 = int(input('Ingrese tercer número: '));
num4 = int(input('Ingrese cuarto número: '));
num5 = int(input('Ingrese quinto número: '));
numbers = [num1, num2, num3, num4, num5];
promedio = float(statistics.mean(numbers));
print(f'El promedio entre {num1}, {num2}, {num3}, {num4}, {num5} es: {promedio}');