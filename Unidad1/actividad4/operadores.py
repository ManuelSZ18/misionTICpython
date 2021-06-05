import random
numeration = 1;
while numeration < 21:       
      x = 1;
      y = 1;
      operations = {'+' : x + y, '-' : x - y, '*' : x * y, '/' : x / y, '**' : x ** y, '%' : x % y, '//' : x // y, '<' : x < y, '>' : x > y, '<=' : x <= y}     
      for operation in operations:
            x = random.randrange(1, 10, 1);
            y = random.randrange(1, 10, 1);  
            operations = {'+' : x + y, '-' : x - y, '*' : x * y, '/' : x / y, '**' : x ** y, '%' : x % y, '//' : x // y, '<' : x < y, '>' : x > y, '<=' : x <= y}
            print ('{}. La operación entre {} {} {} es: {}'.format(numeration, x, operation, y, operations[operation]));            
            numeration = numeration + 1; 