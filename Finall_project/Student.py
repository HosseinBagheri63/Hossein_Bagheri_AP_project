try:
    from Courses import Course
except ModuleNotFoundError:
    from .Courses import Course


class Student:
    def __init__(self, name:str, study_feild:str, faculty:str, courses:dict=None):
        self.name = name
        self.study_feild = study_feild
        self.faculty = faculty
        if courses is None:
            courses = {}
        self.courses = courses

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, value):
        if type(value) is not dict:
            raise TypeError('Courses must be a dictionary')
        for course, grade in value.items():
            self.check_course(course)
            self.check_grade(grade)
        self._courses = value

    @property
    def average(self):
        sum_grades = 0
        sum_units = 0
        for course, grade in self.courses.items():
            if grade is not None:
                sum_grades += grade * course.units
                sum_units += course.units
        if sum_units == 0:
            return None
        return sum_grades / sum_units

    def check_course(self, course):
        if not isinstance(course, Course):
            raise TypeError('Course must be an object of Course subclasses')

    def check_grade(self, grade):
        if grade is not None and type(grade) is not float:
            raise TypeError('Grade must be float')

    def add_course(self, course:Course, grade:float=None):
        self.check_course(course)
        self.check_grade(grade)
        self.courses[course] = grade

    def add_grade(self, course:Course, grade:float):
        self.check_course(course)
        self.check_grade(grade)
        if course not in self.courses:
            raise ValueError('Course is not added')
        self.courses[course] = grade

    def __str__(self):
        courses = []
        for course, grade in self.courses.items():
            courses.append(f"{course.name}:{grade}")
        return f"{self.name} - {courses} - {self.study_feild} - {self.faculty} - {self.average}"
