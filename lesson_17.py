# Создайте функцию is_cat_here(), которая принимает любое количество аргументов
# и проверяет есть ли строка 'cat' среди них. Функция должна возвращать True,
# если такой параметр есть и False в обратном случае. Буквы в строке 'cat' могут быть как большие, так и маленькие


def is_cat_here(*args):
    line = [str(val).lower() for val in list(args)]
    if 'cat' in line:
        return True
    else:
        return False

# Создайте функцию is_item_here(item, *args), которая проверяет есть ли  item среди args.
# Функция должна возвращать True, если такой параметр есть и False в обратном случае.


def is_item_here(item, *args):
    if item in args:
        return True
    else:
        return False

# Создайте функцию your_favorite_color() с позиционным параметром my_color и параметрами **kwargs,
# которая будет выводить на экран 'My favorite color is (значение my_color), what is your favorite color?',
# если в параметрах kwargs нет ключа color, и 'My favorite color is (значение my_color),
# but (значение по ключу color) is also pretty good!', если в параметрах kwargs ключ color присутствует.


def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        return print('My favorite color is {my_color}, but {color} is also pretty good!'
                     .format(my_color=my_color, color=kwargs['color']))
    else:
        return print('My favorite color is {}, what is your favorite color?'.format(my_color))
