from scipy.misc import derivative


def main_func(x):
    """x ** 4 - 2 * x ** 3 - 9 * x ** 2 - 3 * x - 2"""
    return x ** 4 - 2 * x ** 3 - 9 * x ** 2 - 3 * x - 2


def derivative_func(x):
    """4 * x ** 3 - 6 * x ** 2 - 18 * x - 3"""
    return derivative(func=main_func, x0=x)


def bisection_method(a, b, f):
    mid, i = (a + b) / 2, 0
    while abs(f(mid)) >= e and i < 1e3:
        mid, i = (a + b) / 2, i + 1
        a, b = (a, mid) if f(a) * f(mid) <= 0 else (mid, b)
    return (a + b) / 2


def chord_method(a, b, f):
    i = 0
    try:
        while abs(b - a) >= e and i < 1e3:
            a = b - (b - a) * f(b) / (f(b) - f(a))
            b = a - (a - b) * f(a) / (f(a) - f(b))
            i += 1
        return b
    except ZeroDivisionError:
        return b


def newton_method(x0, f, f1):
    x, x_prev, i = x0, x0 + 2 * e, 0
    while abs(x - x_prev) >= e and i < 1e3:
        x, x_prev, i = x - f(x) / f1(x), x, i + 1
    return x


if __name__ == '__main__':
    a1, b1, a2, b2, = 4.0, 5.0, -2.0, -1.5
    e = float(input('Input precision (1e-10 - 1): '))
    while e > 1 or e < 1e-10:
        e = float(input('Input precision (1e-10 - 1): '))

    print(f'Your function: {main_func.__doc__}')
    print(f'The derivative of your function: {derivative_func.__doc__}')
    print(f'For the first interval: [{a1}; {b1}]\n')

    print(f'Bisection method: x = {bisection_method(a1, b1, main_func)}')
    print(f'Chord method: x = {chord_method(a1, b1, main_func)}')
    print(f'Newton method: x = {newton_method(a1, main_func, derivative_func)}\n')

    print(f'For the second interval: [{a2}; {b2}]\n')

    print(f'Bisection method: x = {bisection_method(a2, b2, main_func)}')
    print(f'Chord method: x = {chord_method(a2, b2, main_func)}')
    print(f'Newton method: x = {newton_method(a2, main_func, derivative_func)}\n')

    input("Enter: ")
