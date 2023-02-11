# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def Power(number, power):
    if power == 0:
        return 1
    return Power(number, power-1) * number

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print (f"Результат: {Power(a,b)}")
