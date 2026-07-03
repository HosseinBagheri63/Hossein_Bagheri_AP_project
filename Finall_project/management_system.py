import numpy as np

try:
    from Student import Student
    from Courses import Course
except ModuleNotFoundError:
    from .Student import Student
    from .Courses import Course


class Management_system:
    def __init__(self, students:set=None, courses:set=None):
        if students is None:
            students = set()
        if courses is None:
            courses = set()
        self.students = students
        self.courses = courses

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, value):
        if type(value) is not set:
            raise TypeError('Students must be a set')
        for student in value:
            self.check_student(student)
        self._students = value

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, value):
        if type(value) is not set:
            raise TypeError('Courses must be a set')
        for course in value:
            self.check_course(course)
        self._courses = value

    def check_student(self, student):
        if not isinstance(student, Student):
            raise TypeError('Student must be an object of Student class')

    def check_course(self, course):
        if not isinstance(course, Course):
            raise TypeError('Course must be an object of Course subclasses')

    def add_student(self, student:Student):
        self.check_student(student)
        self.students.add(student)

    def remove_student(self, student:Student):
        self.check_student(student)
        if student not in self.students:
            raise ValueError('Student is not added')
        self.students.remove(student)

    def add_course(self, course:Course):
        self.check_course(course)
        self.courses.add(course)

    def remove_course(self, course:Course):
        self.check_course(course)
        if course not in self.courses:
            raise ValueError('Course is not added')
        self.courses.remove(course)
        for student in self.students:
            if course in student.courses:
                del student.courses[course]

    def add_course_to_student(self, student:Student, course:Course, grade:float=None):
        self.check_student(student)
        self.check_course(course)
        if student not in self.students:
            raise ValueError('Student is not added')
        if course not in self.courses:
            raise ValueError('Course is not added')
        student.add_course(course, grade)

    def add_grade_to_student(self, student:Student, course:Course, grade:float):
        self.check_student(student)
        self.check_course(course)
        if student not in self.students:
            raise ValueError('Student is not added')
        if course not in self.courses:
            raise ValueError('Course is not added')
        student.add_grade(course, grade)

    def student_units(self, student:Student):
        self.check_student(student)
        units = 0
        for course in student.courses:
            units += course.units
        return units

    def merge_sort(self, value:list, key, reverse:bool=False):
        if len(value) <= 1:
            return value
        middle = len(value) // 2
        left = self.merge_sort(value[:middle], key, reverse)
        right = self.merge_sort(value[middle:], key, reverse)
        return self.merge(left, right, key, reverse)

    def merge(self, left:list, right:list, key, reverse:bool=False):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if self.comes_first(left[i], right[j], key, reverse):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    def comes_first(self, first, second, key, reverse:bool=False):
        if reverse:
            return key(first) >= key(second)
        return key(first) <= key(second)

    def sort_students_by_average(self, reverse:bool=False):
        students = list(self.students)
        return self.merge_sort(students, self.average_key, reverse)

    def sort_students_by_name(self, reverse:bool=False):
        students = list(self.students)
        return self.merge_sort(students, self.name_key, reverse)

    def sort_students_by_units(self, reverse:bool=False):
        students = list(self.students)
        return self.merge_sort(students, self.units_key, reverse)

    def average_key(self, student:Student):
        if student.average is None:
            return -1
        return student.average

    def name_key(self, student:Student):
        return student.name

    def units_key(self, student:Student):
        return self.student_units(student)

    def all_grades(self):
        grades = []
        for student in self.students:
            for grade in student.courses.values():
                if grade is not None:
                    grades.append(grade)
        return np.array(grades)

    def grades_average(self):
        grades = self.all_grades()
        if len(grades) == 0:
            return None
        return float(np.mean(grades))

    def grades_standard_deviation(self):
        grades = self.all_grades()
        if len(grades) == 0:
            return None
        return float(np.std(grades))

    def max_grade(self):
        grades = self.all_grades()
        if len(grades) == 0:
            return None
        return float(np.max(grades))

    def min_grade(self):
        grades = self.all_grades()
        if len(grades) == 0:
            return None
        return float(np.min(grades))

    def is_passed(self, student:Student):
        self.check_student(student)
        if student not in self.students:
            raise ValueError('Student is not added')
        if student.average is None:
            return False
        return student.average >= 10

    def student_status(self, student:Student):
        if self.is_passed(student):
            return 'passed'
        return 'failed'
