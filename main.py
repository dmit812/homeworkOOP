class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average = float()

    def rate_hwl(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course\
                in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_rate(self):
        grade_list = sum(self.grades.values(), [])
        self.average = sum(grade_list) / len(grade_list)
        return round(self.average, 1)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}' \
              f' \nСредняя оценка за домашние задания: {self.__average_rate()}' \
              f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.__average_rate() < other.__average_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average = float()

    def __average_rate(self):
        grade_list = sum(self.grades.values(), [])
        self.average = sum(grade_list) / len(grade_list)
        return round(self.average, 1)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.__average_rate()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.__average_rate() < other.__average_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


def average_all_students(student_list, course):
    all_grades = 0
    all_count = 0
    for student in student_list:
        if student.courses_in_progress == [course]:
            all_grades += student.average
            all_count += 1
    average_all = all_grades / all_count
    print(f'\nСредняя оценка студентов за домашние задания по курсу {course}: {round(average_all, 1)}')


def average_all_lecturers(lecturer_list, course):
    all_grades = 0
    all_count = 0
    for lecturer in lecturer_list:
        if lecturer.courses_attached == [course]:
            all_grades += lecturer.average
            all_count += 1
    average_all = all_grades / all_count
    print(f'\nСредняя оценка лекторов за лекции по курсу {course}: {round(average_all, 1)}')


mentor_01 = Mentor('Petr', 'Petrov')
mentor_01.courses_attached += ['Python']

mentor_02 = Mentor('Sergey', 'Popov')
mentor_02.courses_attached += ['Python']

lecturer_01 = Lecturer('Anna', 'Lebedeva')
lecturer_01.courses_attached += ['Python']

lecturer_02 = Lecturer('Jan', 'Human')
lecturer_02.courses_attached += ['Python']

reviewer_01 = Reviewer('Ruby', 'Eman')
reviewer_01.courses_attached += ['Python']

reviewer_02 = Reviewer('Some', 'Buddy')
reviewer_02.courses_attached += ['Python']

student_01 = Student('Ivan', 'Ivanov', 'male')
student_01.courses_in_progress += ['Python']
student_01.finished_courses += ['Введение в программирование']

student_02 = Student('Irina', 'Smirnova', 'female')
student_02.courses_in_progress += ['Python']
student_02.finished_courses += ['GIT']

reviewer_01.rate_hw(student_01, 'Python', 10)
reviewer_01.rate_hw(student_01, 'Python', 9)
reviewer_01.rate_hw(student_01, 'Python', 9)
reviewer_01.rate_hw(student_02, 'Python', 9)
reviewer_01.rate_hw(student_02, 'Python', 8)
reviewer_01.rate_hw(student_02, 'Python', 7)

reviewer_02.rate_hw(student_01, 'Python', 9)
reviewer_02.rate_hw(student_01, 'Python', 8)
reviewer_02.rate_hw(student_01, 'Python', 9)
reviewer_02.rate_hw(student_02, 'Python', 10)
reviewer_02.rate_hw(student_02, 'Python', 7)
reviewer_02.rate_hw(student_02, 'Python', 9)

student_01.rate_hwl(lecturer_01, 'Python', 10)
student_01.rate_hwl(lecturer_01, 'Python', 9)
student_01.rate_hwl(lecturer_01, 'Python', 10)
student_01.rate_hwl(lecturer_02, 'Python', 10)
student_01.rate_hwl(lecturer_02, 'Python', 8)
student_01.rate_hwl(lecturer_02, 'Python', 8)

student_02.rate_hwl(lecturer_01, 'Python', 10)
student_02.rate_hwl(lecturer_01, 'Python', 9)
student_02.rate_hwl(lecturer_01, 'Python', 9)
student_02.rate_hwl(lecturer_02, 'Python', 10)
student_02.rate_hwl(lecturer_02, 'Python', 7)
student_02.rate_hwl(lecturer_02, 'Python', 7)

print(f'Список учителей: \n\n{mentor_01}\n\n{mentor_02}')
print()
print(f'Список рецензентов: \n\n{reviewer_01}\n\n{reviewer_02}')
print()
print(f'Список лекторов: \n\n{lecturer_01}\n\n{lecturer_02}')
print()
print(f'Список студентов: \n\n{student_01}\n\n{student_02}')
print()
print(f'Сравнение лекторов по средней оценке за лекции: {lecturer_01 > lecturer_02}')
print()
print(f'Сравнение студентов по средней оценке за домашние задания: {student_01 < student_02}')
average_all_lecturers([lecturer_01, lecturer_02], 'Python')
average_all_students([student_01, student_02], 'Python')
