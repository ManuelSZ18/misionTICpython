import random
hour = random.randrange(1, 24, 1);
minutes = random.randrange(10, 59, 1);
if hour >= 1 and hour < 12:
    print('Son las {}:{} a.m. - Buenos dias'.format(hour, minutes));
elif hour >= 12 and hour < 18:
    print('Son las {}:{} p.m. - Buenas tardes'.format(hour, minutes));
else:
    print('Son las {}:{} p.m. - Buenas Noches'.format(hour, minutes));