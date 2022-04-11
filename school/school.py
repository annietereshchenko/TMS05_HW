"""""
Создайте класс Students, содержащий поля: фамилия и инициалы, номер группы,
успеваемость (массив из пяти элементов).
Создать класс School:
Добавить возможно для добавления студентов в школу
Добавить возможность вывода фамилий и номеров групп студентов,
имеющих оценки, равные только 5 или 6.
Добавить возможность вывода учеников заданной группы
Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)
"""""


class Students:

    def __init__(self, surname: str, group_number: int, estimates: list):
        self.surname = surname
        self.group_number = group_number
        self.estimates = estimates


class School:

    def __init__(self):
        self.students = list()

    def add_student(self, student):
        self.students.append(student)

    def get_all_students(self):
        return [student for student in self.students]

    def show_student_with_marks(self, *marks):
        students_list = []
        for student in self.students:
            if all([mark in marks for mark in student.estimates]):
                print(f"Student {student.surname} in the "
                      f"{student.group_number} group has only {marks} marks")
                students_list.append(student)
        return students_list

    def show_student_with_group(self, group: int):
        student_list = []
        for student in self.students:
            if student.group_number == group:
                print(f"Student {student.surname} in the group {group}")
                student_list.append(student)
        return student_list

    def show_students_with_automat(self, average_number_for_automat: int):
        students_with_automat = [student for student in self.students
                                  if sum(student.estimates) / len(student.estimates) >= average_number_for_automat]

        for student in students_with_automat:
            print(f"Student {student.surname} has automat")
        return students_with_automat
