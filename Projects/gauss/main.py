def gauss(a, b, dim):

    x = [0] * dim

    for k in range(dim - 1):
        for i in range(k + 1, dim):
            divider = a[i][k] / a[k][k]
            res[i] -= divider * res[k]
            for j in range(k, dim):
                a[i][j] -= divider * a[k][j]

    try:
        for k in range(dim - 1, -1, -1):
            x[k] = (b[k] - sum([a[k][j] * x[j] for j in range(k + 1, dim)])) / a[k][k]
        return x
    except ZeroDivisionError as e:
        print(f'Exception: {e}. So, the system has infinite number of answers or answers don\'t exist...')


if __name__ == '__main__':
    rows_number = int(input('Введіть кількість рядків: '))
    coefs = [[float(input('Введіть число матриці: ')) for i in range(rows_number)] for j in range(rows_number)]
    res = [float(input('Введіть число після дорівнює: ')) for k in range(rows_number)]
    # Дані для мого варіанту:
    # rows_number = 4
    # coefs = [[3.81, 0.25, 1.28, 0.75], [2.25, 1.32, 4.58, 0.49], [5.31, 6.28, 0.98, 1.04], [9.39, 2.45, 3.35, 2.28]]
    # res = [4.21, 6.47, 2.38, 10.48]

    solutions = gauss(coefs, res, rows_number)
    print(solutions)