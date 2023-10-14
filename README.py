class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lectures_grades:
                lecturer.lectures_grades[course] += [grade]
            else:
                lecturer.lectures_grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        avg_grade = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades)
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)
        return f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за домашние задания:{avg_grade}\nКурсы в процессе изучения:{courses_in_progress_str}\nЗавершенные курсы:{finished_courses_str}'
    def __lt__(self, other):
        if not self.grades or not other.grades:
            return False
        avg_grade_self = sum(sum(grades) / len(grades) for grades in self.grades.values()) / len(self.grades)
        avg_grade_other = sum(sum(grades) / len(grades) for grades in other.grades.values()) / len(other.grades)
        return avg_grade_self < avg_grade_other
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_grades = {}
    def __str__(self):
        avg_grade = sum(sum(grades) / len(grades) for grades in self.lectures_grades.values()) / len(self.lectures_grades)
        return f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{avg_grade} '
    
    def __lt__(self, other):
        if not self.lectures_grades or not other.lectures_grades:
            return False
        avg_grade_self = sum(sum(grades) / len(grades) for grades in self.lectures_grades.values()) / len(self.lectures_grades)
        avg_grade_other = sum(sum(grades) / len(grades) for grades in other.lectures_grades.values()) / len(other.lectures_grades)
        return avg_grade_self < avg_grade_other
    
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
        return f'Имя:{self.name}\nФамилия:{self.surname} '
    
def average_hw_grade(students, course):
    total_grade = 0
    total_students = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            total_students += len(student.grades[course])
    if total_students > 0:
        return total_grade / total_students
    else:
        return 0

def average_lecture_grade(lecturers, course):
    total_grade = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.lectures_grades:
            total_grade += sum(lecturer.lectures_grades[course])
            total_lecturers += len(lecturer.lectures_grades[course])
    if total_lecturers > 0:
        return total_grade / total_lecturers
    else:
        return 0

best_student0 = Student('Ruoy', 'Eman', 'your_gender')
best_student0.courses_in_progress += ['Python']
best_student0.finished_courses += ['Java']

best_student1 = Student('Rick', 'Sanchez', 'your_gender')
best_student1.courses_in_progress += ['PHP']
best_student1.finished_courses += ['Java']

cool_mentor0 = Reviewer('Some', 'Buddy')
cool_mentor0.courses_attached += ['Python']

cool_mentor1 = Reviewer('Som', 'Buddy')
cool_mentor1.courses_attached += ['PHP']

cool_lecturer0 = Lecturer('Another', 'Buddy')
cool_lecturer0.courses_attached += ['Python']

cool_lecturer1 = Lecturer('New', 'Buddy')
cool_lecturer1.courses_attached += ['PHP']

best_student0.rate_lecturer(cool_lecturer0, 'Python', 8)
best_student0.rate_lecturer(cool_lecturer0, 'Python', 10)

cool_mentor0.rate_hw(best_student0, 'Python', 10)
cool_mentor0.rate_hw(best_student0, 'Python', 9)

cool_mentor1.rate_hw(best_student0, 'PHP', 1)
cool_mentor1.rate_hw(best_student0, 'PHP', 9)

best_student1.rate_lecturer(cool_lecturer1, 'PHP', 4)
best_student1.rate_lecturer(cool_lecturer1, 'PHP', 7)

print(cool_mentor0)
print()
print(cool_lecturer0)
print()
print(best_student0)
print()

if best_student0 < best_student1:
    print(f"{best_student0.name} {best_student0.surname} учится лучше чем {best_student1.name} {best_student1.surname}")
else:
    print(f"{best_student1.name} {best_student1.surname} учится лучше чем {best_student0.name} {best_student0.surname}")

if cool_lecturer0 < cool_lecturer1:
    print(f"{cool_lecturer0.name} {cool_lecturer0.surname} лучший лектор, чем {cool_lecturer1.name} {cool_lecturer1.surname}")
else:
    print(f"{cool_lecturer1.name} {cool_lecturer1.surname} лучший лектор, чем {cool_lecturer0.name} {cool_lecturer0.surname}")

print()

students = [best_student0, best_student1]
lecturers = [cool_lecturer0, cool_lecturer1]

average_hw = average_hw_grade(students, 'Python')
average_lecture = average_lecture_grade(lecturers, 'Python')

print(f"Средняя оценка за домашние задания по курсу 'Python': {average_hw}")
print(f"Средняя оценка за лекции по курсу 'Python': {average_lecture}")