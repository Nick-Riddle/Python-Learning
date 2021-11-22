import copy


# Дані для мого варіанту:
# rows_number = 5
# coefs = [[5.18, 1.12, 0.95, 1.32, 0.83],
#          [0, -20.916, -9.9176, -1.4742, -3.7842],
#          [0.95, 2.12, 6.13, 1.29, 1.57],
#          [1.32, 0.57, 1.29, 4.57, 1.25],
#          [0.83, 0.91, 1.57, 1.25, 5.21]]
#
# res = [6.19, -9.695, 4.28, 6.25, 4.95]


def iteration_method(size, a, b):
    try:
        x = [0 for i in range(size)]
        for iteration in range(1, 5):
            x_next = copy.copy(a)
            for i in range(size):
                s1 = sum(a[i][j] * x_next[j] for j in range(i))
                s2 = sum(a[i][j] * x[j] for j in range(i + 1, size))
                x_next[i] = (b[i] - s1 - s2) / a[i][i]
            x = x_next
            print(f'Розв\'язок системи (ітерація {iteration}): {x}')
    except:
        print(f'ERROR.')


if __name__ == '__main__':
    rows_number = int(input('Введіть кількість рядків: '))
    coefs = [[float(input('Введіть число матриці: ')) for i in range(rows_number)] for j in range(rows_number)]
    res = [float(input('Введіть число після дорівнює: ')) for k in range(rows_number)]

    iteration_method(rows_number, coefs, res)

    input('Нажміть Enter для виходу...')

