# Создайте функцию-генератор get_week_day(), которая создаёт генератор,
# вырабатывающий один день недели за раз,
# Дни недели должны начинаться с воскресенья и заканчиваться субботой.


def get_week_day():
    week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for day in week:
        yield day
