import random
for i in range(0, 20):
      x = random.randrange(1, 10, 1);
      y = random.randrange(1, 10, 1);   
      operators = ['+', '-', '*', '/', '//', '%', '**', '>', '<', '<=', '+', '-', '*', '/', '//', '%', '**', '>', '<', '>='];
      operations = [x + y, x - y, x * y, x / y, x // y, x % y, x ** y, x > y, x < y, x >= y, x + y, x - y, x * y, x / y, x // y, x % y, x ** y, x > y, x < y, x >= y];
      numeration = i + 1;   
      print('{}. La operación entre {} {} {} es: '.format(numeration, x, operators[i], y) + str(operations[i]));