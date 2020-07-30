import calendar
print('1.only the month of particular year')
print('2.all the months of that particular year')
r = int(input('enter any option:'))
if r == 1:
    n = int(input('enter the year:'))
    m = int(input('enter the month:'))
    print(calendar.month(n,m))
elif r == 2:
    n = int(input('enter the year:'))
    print(calendar.calendar(n))
else:
    print('sorry the option is out of bound')
