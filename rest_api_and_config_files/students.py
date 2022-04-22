# Разработайте поиск учащихся в одном классе, посещающих одну секцию.
# Фильтрацию учащихся по их полу. Поиск ученика по имени(часть имени)
import json


def search(class_number=None, club=None, gender=None, name=None):
    with open('students.json') as f:
        student_list = json.load(f)
    for student in student_list:
        if student['Class'] == class_number and student['Club'] == club:
            print(student)
        if student['Gender'] == gender:
            print(student)
        if name and name in student['Name']:
            print(student)


print('Студенты класса, посещающие одну секцию')
search(class_number='3a', club='Chess')
print('Фильтр по полу')
search(gender='M')
print('Поиск по имени')
search(name='Hayato')
