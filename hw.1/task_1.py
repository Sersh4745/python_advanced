'''1. Программа принимает от пользователя диапазоны для коэффициентов a, b, c квадратного уравнения: ax2 + bx + c = 0. 
Перебирает все варианты целочисленных коэффициентов в указанных диапазонах, определяет квадратные уравнения, которые имею решение

Пример выполнения:

a1: -2
a2: 2
b1: -3
b2: 1
c1: 0
c2: 4

-2 -3 0 Yes -0.0 -1.5
-2 -3 1 Yes 0.28 -1.78
-2 -3 2 Yes 0.5 -2.0
-2 -3 3 Yes 0.69 -2.19
-2 -3 4 Yes 0.85 -2.35
-2 -2 0 Yes -0.0 -1.0
-2 -2 1 Yes 0.37 -1.37
-2 -2 2 Yes 0.62 -1.62
-2 -2 3 Yes 0.82 -1.82
'''

import math

print("Введите коэффициенты для уровнения ax^2 + bx + c = 0: ")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# discr = b ** 2 - 4 * a * c
# print("Дискриминант D = %.2f" % discr)

# if discr > 0:
#     x1 = (-b + math.sqrt(discr)) / (2 * a)
#     x2 = (-b - math.sqrt(discr)) / (2 * a)
#     print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
# elif discr == 0:
#     x = -b / (2 * a)
#     print("x = %.2f" % x)
# else:
#     print("Корней нет") 

discriminant = b**2 - 4*a*c
print('Дискриминант = ' + str(discriminant))
if discriminant < 0:
    print('Корней нет')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print(f'x1 = {round(x1,2)}\nx2 = {round(x2,2)}')


