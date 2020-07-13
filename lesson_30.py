# Создайте функцию-декоратор wait, которая задерживает выполнение кода функции, которую она декорирует, на n секунд.
# Аргумент n должен передаваться в декоратор. Воспользуйтесь функцией для задержки выполнения кода.
# Найдите информацию об использовании этой функции в интернете самостоятельно. Также после задержки должно
# выводится сообщение "There was a pause {количество секунд} seconds before execution {имя задекорированной функции }"

from functools import wraps
from time import sleep


def wait(seconds):
    def inner_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(seconds)
            print(f"There was a pause {seconds} seconds before execution {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return inner_wrapper
