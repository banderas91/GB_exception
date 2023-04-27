def method1():
    try:
        a = 1 / 0
    except ZeroDivisionError:
        print("На ноль делить нельзя!")


def method2():
    try:
        b = "строка" + 5
    except TypeError:
        print("Нельзя сложить строку и число!")


def method3():
    try:
        c = [1, 2, 3]
        print(c[5])
    except IndexError:
        print("Индекс вне диапазона!")
