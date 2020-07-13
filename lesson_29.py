# Создайте функцию-декоратор prohibit_more_than_2_args, которая выполняет функцию, которую она декорирует,
# если в этой функции не больше двух аргументов. В противном случае должна вызываться ошибка
# ValueError с сообщением "Function must have less than 3 arguments!"

from functools import wraps


def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            raise ValueError('Function must have less than 3 arguments!')
        return func(*args, **kwargs)
    return wrapper
