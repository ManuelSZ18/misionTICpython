import random
indexOperations = 0;
point = 1;
for i in ['+', '-', '*', '/', '//', '%', '**', '>', '<', '<=', 
          '+', '-', '*', '/', '//', '%', '**', '>', '<', '>=']:  
    x = random.randrange(1, 10, 1);
    y = random.randrange(1, 10, 1);   
    operations = [x + y, x - y, x * y, x / y, x // y, x % y, x ** y, x > y, x < y, x >= y, 
                  x + y, x - y, x * y, x / y, x // y, x % y, x ** y, x > y, x < y, x >= y];   
    print('{}. La operación entre {} {} {} es: '.format(point, x, i, y) + str(operations[indexOperations]));
    indexOperations = indexOperations + 1;
    point = point + 1;    