import calendar
print ('Добро пожаловать в календарь\n')

year = int(input('Пожалуйста введите будующий год: '))
month = int(input('Введите номер месяца: '))

print (calendar.month(year, month))

print ('Дозвидания')