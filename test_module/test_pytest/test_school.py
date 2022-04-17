from school import Students, School
import pytest


class TestForSchool:

    @pytest.fixture()
    def setUp(self):
        self.school = School()
        self.dzima = Students("Sadouski", 1, [5, 6, 5, 5, 6])
        self.nikita = Students("Ronaldo", 1, [7, 7, 7, 7, 7])
        self.sergey = Students("Sheva", 2, [8, 8, 8, 8, 8])
        self.artem = Students("Sosna", 2, [2, 10, 5, 6, 2])
        self.sasha = Students("Saga", 1, [6, 6, 6, 6, 6])

    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.regression
    def test_get_students(self, setUp):
        self.school.add_student(self.dzima)
        self.school.add_student(self.nikita)
        number_of_added_students = len(self.school.get_all_students())
        assert number_of_added_students == 2

    @pytest.mark.regression
    def test_get_students_empty_school(self, setUp):
        number_of_added_students = len(self.school.get_all_students())
        assert number_of_added_students == 0

    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.regression
    def test_get_students_with_certain_marks(self, setUp):
        self.school.add_student(self.dzima)
        self.school.add_student(self.nikita)
        number_of_students_with_marks = len(self.school.show_student_with_marks(5, 6))
        assert number_of_students_with_marks == 1

    @pytest.mark.critical_path
    @pytest.mark.regression
    def test_get_students_with_one_certain_mark(self, setUp):
        """""
        Здесь возьмем студента sasha, у которого все оценки только 6 в списке.
        Но подавать на вход будет две оценки 5 и 6
        Проверять студента, у которого только 5 в списке, наверное, не имеет
        смысла
        """""
        self.school.add_student(self.sasha)
        number_of_students_with_mark = len(self.school.show_student_with_marks(5, 6))
        assert number_of_students_with_mark == 1

    @pytest.mark.critical_path
    @pytest.mark.regression
    def test_get_students_with_not_all_certain_marks(self, setUp):
        """""
        Здесь возьмем студента artem, у которого есть оценки 5 и 6 в списке,
        но так же у него есть другие оценки
        """""
        self.school.add_student(self.artem)
        number_of_students_with_marks = len(self.school.show_student_with_marks(5, 6))
        assert number_of_students_with_marks == 0

    @pytest.mark.regression
    def test_get_students_with_certain_marks_empty_school(self, setUp):
        number_of_students_with_marks = len(self.school.show_student_with_marks(5, 6))
        assert number_of_students_with_marks == 0

    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.regression
    @pytest.mark.parametrize('group_number, expected_result', [(2, 2), (1, 1)])
    def test_param(self, group_number, expected_result, setUp):
        self.school.add_student(self.sergey)
        self.school.add_student(self.artem)
        self.school.add_student(self.nikita)
        number_of_students_in_group = len(self.school.show_student_with_group(group_number))
        assert number_of_students_in_group == expected_result

    @pytest.mark.regression
    def test_get_students_with_non_existent_group(self, setUp):
        self.school.add_student(self.sergey)
        self.school.add_student(self.artem)
        self.school.add_student(self.nikita)
        number_of_students_in_group = len(self.school.show_student_with_group(3))
        assert number_of_students_in_group == 0

    @pytest.mark.regression
    def test_get_students_with_group_empty_school(self, setUp):
        number_of_students_in_group = len(self.school.show_student_with_group(1))
        assert number_of_students_in_group == 0

    @pytest.mark.critical_path
    @pytest.mark.regression
    def test_get_students_with_automat_lower_bound(self, setUp):
        """""
        Здесь воспользуемся методом граничных значений
        Средняя оценка для автомата - 7
        Возьмем студента со следующим средним баллом -
        6
        """""
        self.school.add_student(self.sasha)
        number_of_students_with_automat = len(self.school.show_students_with_automat(7))
        assert number_of_students_with_automat == 0

    @pytest.mark.smoke
    @pytest.mark.critical_path
    @pytest.mark.regression
    def test_get_students_with_automat_bound(self, setUp):
        """""
        Здесь воспользуемся методом граничных значений
        Средняя оценка для автомата - 7
        Возьмем студента со следующим средним баллом -
        7
        """""
        self.school.add_student(self.nikita)
        number_of_students_with_automat = len(self.school.show_students_with_automat(7))
        assert number_of_students_with_automat == 1

    @pytest.mark.critical_path
    @pytest.mark.regression
    def test_get_students_with_automat_upper_bound(self, setUp):
        """""
        Здесь воспользуемся методом граничных значений
        Средняя оценка для автомата - 7
        Возьмем студента со следующим средним баллом -
        8
        """""
        self.school.add_student(self.sergey)
        number_of_students_with_automat = len(self.school.show_students_with_automat(7))
        assert number_of_students_with_automat == 1

    @pytest.mark.regression
    def test_get_students_with_automat_empty_school(self, setUp):
        number_of_students_with_automat = len(self.school.show_students_with_automat(7))
        assert number_of_students_with_automat == 0
