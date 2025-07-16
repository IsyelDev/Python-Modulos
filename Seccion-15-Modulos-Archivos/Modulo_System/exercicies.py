import calendar
from datetime import datetime

current_date = datetime.now()
print(f'Fecha actual: {current_date}')


days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
day_index = current_date.weekday()
print(day_index)

nuevo_dia = days[day_index]
print(nuevo_dia)

if calendar.isleap(current_date.year):
      print(f'{current_date.year} es un año bisiesto')
else:
    print(f'{current_date} no es bisiesto')
    
print('Calendario del mes actual')
print(calendar.month (current_date.year , current_date.month))


first_weekday, days_in_month = calendar.monthrange(current_date.year, current_date.month)
print(days[first_weekday])
print(days_in_month)
