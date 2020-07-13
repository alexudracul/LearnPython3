# Из исходного списка greetings = ['hello', 'hi', 'hey', 'hola']
# создайте новый список содержащий вторую букву из каждой строки исходного списка.
# Выведите новый список на печать.
#
# Решите задание двумя способами - при помощи List Comprehension и без него.

greetings = ['hello', 'hi', 'hey', 'hola']

new_greetings_1 = [word[1] for word in greetings]
print(new_greetings_1)

new_greetings_2 = []
for word in greetings:
    new_greetings_2.append(word[1])
print(new_greetings_2)

# Из исходного списка digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# создайте новый список содержащий нечетные числа исходного списка.
# Выведите новый список на печать.
#
# Решите задание двумя способами - при помощи List Comprehension и без него.

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_digits_1 = [number for number in digits if number & 1]
print(new_digits_1)

new_digits_2 = []
for number in digits:
    if number % 2 != 0:
        new_digits_2.append(number)
print(new_digits_2)
