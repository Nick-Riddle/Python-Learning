"""
пока counter (количество делителей) не будет равен 500:
    Считать треугольные числа
    в цикле от 1 до треугольного числа находим делители числа:
        если треугольное число делится на элемент перебора цикла:

    к counter2 (следующее натуральное число) додавать единицу
"""

counter = 0
counter2 = 1
sum = 76576499
while counter <= 500:
    sum += counter2
    for i in range(1, sum + 1):
        if sum % i == 0:
            counter += 1
    if counter >= 500:
        print(sum)
    else:
        counter = 0
        counter2 += 1