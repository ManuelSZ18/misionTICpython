hour = 15;
"""En este punto se evalua si el valor almacenado en la variable es superior a la hora maxima del dia que es 24"""
if hour > 24:
    print('La hora proporcionada es inválida!');
# Aqui se evalua nuevamente si el valor almacenado corresponde a la franja de noche
elif hour > 17:
    print(f'Son las {hour} a.m.- Buenas Noches!');
# Aqui se evalua nuevamente si el valor almacenado corresponde a la franja de de la tarde
elif hour > 11:
    print(f'Son las {hour} p.m.- Buenas tardes!');
# Aqui se evalua nuevamente si el valor almacenado corresponde a la franja de de la mañana
elif hour > -1:
    print(f'Son las {hour} p.m.- Buenos Dias!');
# Aqui se evalua nuevamente si el valor almacenado corresponde a una hora que no es acorde a las horas predeterminadas del día
else:
    print('La hora proporcionada es inválida!');