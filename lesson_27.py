# Создайте функцию-декоратор print_args, которая распечатывает
# аргументы *args и **kwargs функции, которую она декорирует


def print_args(func):
    def wrapper(*args, **kwargs):
        print('args: ', args)
        print('kwargs: ', kwargs)
        return func(*args, **kwargs)
    return wrapper


@print_args
def my_func(num):
    print(num * num)
