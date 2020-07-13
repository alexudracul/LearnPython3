# Создайте функции cat_voice() and dog_voice(), которые выводят на экран 'Meow!' и 'Woof!' соответственно.
# Сделайте по одному вызову каждой из функций


def cat_voice():
    print('Meow!')


def dog_voice():
    print('Woof!')


cat_voice()
dog_voice()

# Создайте функции cat_voice() and dog_voice(), которые возвращают значения 'Meow!' и 'Woof!' соответственно.
# Выведите на экран 'Meow!' и 'Woof!' по 2 раза


def cat_voice():
    return 'Meow!'


def dog_voice():
    return 'Woof!'


print(cat_voice())
print(cat_voice())
print(dog_voice())
print(dog_voice())


# Создайте функцию get_voice() которая возвращает передаваемый ей в качестве параметра текст c восклицательным знаком.


def get_voice(text):
    return str(text) + '!'


# Создайте функцию, которая генерирует последовательность нечетных чисел в диапазоне от a до b (a и b включительно).
# Значения a и b должны передаваться в качестве параметров. Результирующая последовательность должна возвращаться
# в форме объекта list. Решите задание двумя способами - при помощи List Comprehension  и без него.

# With List Comprehension
def get_odd_numbers_list(a=0, b=0):
    return [number for number in range(a, b+1) if number % 2 == 1]


# Without List Comprehension
def get_odd_numbers_list(a=0, b=0):
    odd_list = []
    for number in range(a, b+1):
        if number % 2 == 1:
            odd_list.append(number)
    return odd_list
