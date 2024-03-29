import unittest
from school import Students, School


class TestForSchool(unittest.TestCase):

    def setUp(self) -> None:
        self.school = School()
        self.dzima = Students("Sadouski", 1, [5, 6, 5, 5, 6])
        self.nikita = Students("Ronaldo", 1, [7, 7, 7, 7, 7])
        self.sergey = Students("Sheva", 2, [8, 8, 8, 8, 8])
        self.artem = Students("Sosna", 2, [2, 10, 5, 6, 2])
        self.sasha = Students("Saga", 1, [6, 6, 6, 6, 6])

    def test_get_students(self):
        self.school.add_student(self.dzima)
        self.school.add_student(self.nikita)
        number_of_added_students = len(self.school.get_all_students())
        self.assertEqual(number_of_added_students, 2)

    def test_get_students_empty_school(self):
        number_of_added_students = len(self.school.get_all_students())
        self.assertEqual(number_of_added_students, 0)

    def test_get_students_with_certain_marks(self):
        self.school.add_student(self.dzima)
        self.school.add_student(self.nikita)
        number_of_students_with_marks = len(self.school.show_student_with_marks(5, 6))
        self.assertEqual(number_of_students_with_marks, 1)

    def test_get_students_with_one_certain_mark(self):
        """""
        Здесь возьмем студента sasha, у которого все оценки только 6 в списке.
        Но подавать на вход будет две оценки 5 и 6
        Проверять студента, у которого только 5 в списке, наверное, не имеет
        смысла
        """""
        self.school.add_student(self.sasha)
        number_of_students_with_mark = len(self.school.show_student_with_marks(5, 6))
        self.assertEqual(number_of_students_with_mark, 1)

    def test_get_students_with_not_all_certain_marks(self):
        """""
        Здесь возьмем студента artem, у которого есть оценки 5 и 6 в списке,
        но так же у него есть другие оценки
        """""
        self.school.add_student(self.artem)
        number_of_students_with_marks = len(self.school.show_student_with_marks(5, 6))
        self.assertEqual(number_of_students_with_marks, 0)

    def test_get_students_with_certain_marks_empty_school(self):
        number_of_students_with_marks = len(self.school.show_student_with_marks(5, 6))
        self.assertEqual(number_of_students_with_marks, 0)

    def test_get_students_with_group(self):
        self.school.add_student(self.sergey)
        self.school.add_student(self.artem)
        self.school.add_student(self.nikita)
        number_of_students_in_group = len(self.school.show_student_with_group(2))
        self.assertEqual(number_of_students_in_group, 2)

    def test_get_students_with_non_existent_group(self):
        self.school.add_student(self.sergey)
        self.school.add_student(self.artem)
        self.school.add_student(self.nikita)
        number_of_students_in_group = len(self.school.show_student_with_group(3))
        self.assertEqual(number_of_students_in_group, 0)

    def test_get_students_with_group_empty_school(self):
        number_of_students_in_group = len(self.school.show_student_with_group(1))
        self.assertEqual(number_of_students_in_group, 0)

    def test_get_students_with_automat_lower_bound(self):
        """""
        Здесь воспользуемся методом граничных значений
        Средняя оценка для автомата - 7
        Возьмем студента со следующим средним баллом -
        6
        """""
        self.school.add_student(self.sasha)
        number_of_students_with_automat = len(self.school.show_students_with_automat(7))
        self.assertEqual(number_of_students_with_automat, 0)

    def test_get_students_with_automat_bound(self):
        """""
        Здесь воспользуемся методом граничных значений
        Средняя оценка для автомата - 7
        Возьмем студента со следующим средним баллом -
        7
        """""
        self.school.add_student(self.nikita)
        number_of_students_with_automat = len(self.school.show_students_with_automat(7))
        self.assertEqual(number_of_students_with_automat, 1)

    def test_get_students_with_automat_upper_bound(self):
        """""
        Здесь воспользуемся методом граничных значений
        Средняя оценка для автомата - 7
        Возьмем студента со следующим средним баллом -
        8
        """""
        self.school.add_student(self.sergey)
        number_of_students_with_automat = len(self.school.show_students_with_automat(7))
        self.assertEqual(number_of_students_with_automat, 1)

    def test_get_students_with_automat_empty_school(self):
        number_of_students_with_automat = len(self.school.show_students_with_automat(7))
        self.assertEqual(number_of_students_with_automat, 0)


if __name__ == '__main__':
    unittest.main()
