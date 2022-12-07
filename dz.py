from math import *

a = int(input('ВВедите коэффициент а: '))
b = int(input('ВВедите коэффициент b: '))
c = int(input('ВВедите коэффициент c: '))

discriminant = b**2 - 4*a*c
if discriminant > 0:
    x1 = (-b + sqrt(discriminant))/(2*a)
    x2 = (-b - sqrt(discriminant))/(2*a)
    print('ответ ', x1, x2)
elif discriminant == 0:
    x = -b/(2*a)
    print('ответ ', x)
else:
    print('Ответа нет!')