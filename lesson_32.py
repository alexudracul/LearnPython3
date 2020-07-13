from csv import DictReader


def print_students():
    with open('students.csv', 'r') as file:
        reader = DictReader(file)
        for student in reader:
            print(student)


print_students()
