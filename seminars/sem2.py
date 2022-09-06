from math import factorial
import random

# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# num = '10,56321'
# num=num.replace(',','')
# res = 0
# for i in num:
#     res = res + int(i)
# print(res)

# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# n = int(input('Введите число: '))
# i = 1
# while i <= n:
#     print(factorial(i), end = ' ')
#     i += 1

# Задача 3. Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму
# k = int(input('Введите число: '))
# my_list = []

# for i in range (1, k + 1):
#     my_list.append(round((1 + 1/i)**i, 2))
# print("Получившийся список: ", my_list)

# summ = 0 # Также можно найти сумму элементов при помощи встроенной функции sum(my_list)
# for j in my_list:
#     summ = summ + j
# print("Сумма элементов списка равна", summ)

# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# n = int(input('Введите число: '))
# myList = []
# result = 1
# userList = []

# for i in range(0, n):
#     myList.append(random.randint(-n, n))
# print(myList)

# userInput = input(f"Введите числа от 0 до {n} через пробел: ")
# for el in userInput.split():
#     userList.append(int(el))

# for i in userList:
#     result = result * myList[int(i)]
# print("Произведение элементов на указанных позициях равно: ", result)

# Задача 5. Реализуйте алгоритм перемешивания списка.

# my_list=[1,3,2,4,5,6]
# random.shuffle(my_list)
# print(my_list)