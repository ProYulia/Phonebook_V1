# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
""" num = int(input('Введите день недели: '))
if 1 <= num <= 5:
    print('No')
elif num == 6 or num == 7:
    print('Yes')
else:
    print('Incorrect input') """

# Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
""" x = input('x --> ')
y = input('y --> ')
z = input('z --> ')

expression1 = not(x or y or z)
expression2 = not x or not y or not z
result = expression1 == expression2
print(result) """

# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
""" x = int(input('x --> '))
y = int(input('y --> '))

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
else:
    print('X и Y не должны быть равны нулю') """

# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
""" num = int(input('Введите номер четверти: '))
if num == 1:
    print('x > 0 and y > 0')
elif num == 2:
    print('x < 0 and y > 0')
elif num == 3:
    print('x < 0 and y < 0')
elif num == 4:
    print('x > 0 and y < 0')
else:
    print('Don\'t do stupid things!') """

# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
from cmath import sqrt


""" x1 = float(input('x1 -->'))
y1 = float(input('y1 --> '))
x2 = float(input('x2 --> '))
y2 = float(input('y2 --> '))
result = sqrt((x2 - x1)** 2 +(y2 -y1) ** 2)
result = round(float(result.real),2)
print("Расстояние между точками:", result) """

