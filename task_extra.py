# задача калькулятор необязательная.
# Решать только через рекурсию!. Пользоваться встроенными функциями вычисления таких выражений нельзя, если только для проверки вашего алгоритма.
# на вход подается строка из операторов / * + - и целых чисел. Надо посчитать результат введенного выражения.
# Например,

# на входе
# 1+9/3*7-4
# на выходе
# 18
def MakeCount(num1, num2, action):
    if action == '/':
        if num1 == 0:
            return 0
        return MakeCount(num1 - num2, num2, action) +1
    if action == '*':
        if num2 == 0:
            return 0
        return MakeCount(num1, MakeCount(num1, num2 - 1, action), '+')
    if action == '+':
        if num2 == 0:
            return num1
        return MakeCount(num1, num2 - 1, action) + 1    
    if action == '-':
        if num2 == num1:
            return 0
        return MakeCount(num1 - 1, num2, action) + 1   
    

seq = (input("Введите выражение:"))

list_seq = []
stack = ''
operations = {'*','/','+','-'}
for i in seq: #Работает только для положительных чисел
    if i not in operations:
        stack += i
    else:
        list_seq.append(int(stack))
        list_seq.append(i)
        stack = ''
list_seq.append(int(stack))

for priority in range(2):
    for i in list_seq:
        if i == '*' or i == '/' or ((i == '+' or i == '-') and priority == 1):
            list_seq[list_seq.index(i)+1] = MakeCount (list_seq[list_seq.index(i)-1], list_seq[list_seq.index(i)+1], i)
            list_seq[list_seq.index(i)-1] = ''
            list_seq[list_seq.index(i)] = ''
    list_seq = list(filter(None, list_seq))

print (f"Результат выражения : {list_seq[0]}")