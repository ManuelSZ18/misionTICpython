import random
indexOperations = 0;
point = 1;
for i in ['+', '-', '*', '/', '//', '%', '**', '>', '<', '<=', '+', '-', '*', '/', '//', '%', '**', '>', '<', '>=']:  
    firstTerm = random.randrange(1, 10, 1);
    secondTerm = random.randrange(1, 10, 1);   
    operations = [firstTerm + secondTerm, firstTerm - secondTerm, firstTerm * secondTerm, firstTerm / secondTerm, firstTerm // secondTerm, 
                  firstTerm % secondTerm, firstTerm ** secondTerm, firstTerm > secondTerm, firstTerm < secondTerm, firstTerm >= secondTerm, 
                  firstTerm + secondTerm, firstTerm - secondTerm, firstTerm * secondTerm, firstTerm / secondTerm, firstTerm // secondTerm, 
                  firstTerm % secondTerm, firstTerm ** secondTerm, firstTerm > secondTerm, firstTerm < secondTerm, firstTerm >= secondTerm];   
    print('{}. La operación entre {} {} {} es: '.format(point, firstTerm, i, secondTerm) + str(operations[indexOperations]));
    indexOperations = indexOperations + 1;
    point = point + 1;    