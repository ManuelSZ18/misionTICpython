import random
hour = random.randrange(1, 24, 1);
if hour >= 1 and hour < 12:
    print(f'Son las {hour} horas - Buenos dias!')
if hour >= 12 and hour < 18:
    print(f'Son las {hour} horas - Buenas tardes!')
if hour >= 18 and hour <= 24:
    print(f'Son las {hour} horas - Buenas noches!')