from random import shuffle
from time import perf_counter

questions = [
        ['1+1=1', 'F'],
        ['2+2=4', 'T'],
        ['a = b', 'F'],
        ['Lorem ipsum is false?', 'F'],
        ['True', 'T'],
        ['2 + 2 * 2 = 6', 'T'],
        ['"Aa" * 2 = "AaAa"', 'T'],
        ['False', 'F']
    ]

shuffle(questions)
user_score = 0
start_time = perf_counter()

for question in questions:
    print('True of False:', question[0])
    user_answer = input('Please enter T if it is true and F if it is false: ')
    if str(user_answer.upper()) == question[1]:
        print('Excellent!')
        user_score += 1
    else:
        print('Not correct :( Maybe you will be lucky next time!')
else:
    print('Congratulations! Your total score is: ' + str(user_score) +
          ', total time is:', perf_counter() - start_time, 'seconds')
