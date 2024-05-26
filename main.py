from statistics import mean # импортируем функцию для решения задачи "Среднее арифметическое"
# Задача "Длинна слова"
def WordLen(): # функция используется для определения переменной "а" как локальной
    a = "stroka"
    print(len(a))
WordLen()
# Задача "суммы и разности"
first = 2
second = 3
third = 5 # определяем переменну для задачи "Средее арифметическое"
summa = first + second
diff = first - second
print(first, "+", second, "=", summa, '\n', first, "-", second, "=", diff)
# Задача "Среднее орифметическое"
mass = [first,second,third]
mean = mean(mass)
print(round(mean,2))
#  Задача "Простые строки"
first_string = "Вторник"
second_string = "Понедельник"
print (second_string+", "+first_string)
# Задача "Сложная формула"
a = 3
b = 4
c = 5
f = ((a*b)+(a*c))** 3
print(f/2)


