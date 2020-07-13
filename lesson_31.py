# Создайте функцию add_student(), которая принимает в качестве параметров имя, фамилию и возраст
# и добавляет запись в файл students.csv. При необходимости воспользуйтесь поиском информации в интернете

from csv import writer


def add_student(first_name, last_name, age):
    with open('students.csv', 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow([first_name, last_name, age])
