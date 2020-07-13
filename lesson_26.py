# Создайте функцию, возвращающую генератор, бесконечно вырабатывающий квадраты целых чисел, начиная с 1


def get_infinite_square_generator():
    x = 1
    while True:
        yield x ** 2
        x += 1
