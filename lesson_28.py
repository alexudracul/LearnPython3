# Создайте функцию-декоратор hello_from_decorator, которая добавляет к возвращаемому значению функции,
# которую она декорирует, строку "Hello from decorator!"

from functools import wraps


def hello_from_decorator(func):
    @wraps(func)
    def hello(*args, **kwargs):
        print(str(func(*args, **kwargs)) + ' Hello from decorator!')
    return hello
