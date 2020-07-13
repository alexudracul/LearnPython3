# Создайте функцию even_odd(), создающую генератор, который будет попеременно вырабатывать строки 'even' и 'odd'.


def even_odd():
    x = 1
    while True:
        yield 'odd' if x % 2 == 0 else 'even'
        x += 1


even_odd_generator = even_odd()

i = 0
while i < 100:
    print(i, ' ', next(even_odd_generator))
    i += 1
