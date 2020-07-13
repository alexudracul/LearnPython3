user_input = input('Enter any number')
if user_input == '7':
    print('7 is a lucky number! Today is your lucky day!')
else:
    print('Thank you! Have a nice day!')


user_input = input('Enter an integer number')
try:
    val = int(user_input)
    if val % 2 == 0:
        print('The number is even')
    else:
        print('The number is odd')
except ValueError:
    print("Value is not an integer number. Please try again.")

# OR

print('Enter an integer number')
a = int(input())
print("The number is odd" if a & 1 else "The number is even")
