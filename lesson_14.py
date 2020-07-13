even_sum = 0
for number in range(10, 31):
    if number % 2 == 0:
        even_sum += number
print(even_sum)


user_input = input('Enter an integer number')
for _ in range(int(user_input)):
    print('Hello!')
