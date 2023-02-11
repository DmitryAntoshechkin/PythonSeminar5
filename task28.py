# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def Summa(a, b):
    if b == 0:
        return a
    return Summa(a, b - 1) + 1

a = int(input('Введите число A: '))
b = int(input('Введите число В: '))
print (f"Результат: {Summa(a,b)}")