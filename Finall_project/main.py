import json
from pathlib import Path

try:
    from Courses import Course, Practical_course, Theoretical_course, Presentation_course
    from Student import Student
    from management_system import Management_system
except ModuleNotFoundError:
    from .Courses import Course, Practical_course, Theoretical_course, Presentation_course
    from .Student import Student
    from .management_system import Management_system


DATA_DIR = Path(__file__).parent / 'data'
DATA_FILE = DATA_DIR / 'education_system.json'


def course_to_dict(course):
    data = {
        'class_name': course.__class__.__name__,
        'id': course.id,
        'name': course.name,
        'teacher': course.teacher,
        'department': course.department,
        'course_type': course.course_type,
        'units': course.units,
        'class_times': course.class_times,
        'class_room': course.class_room,
        'exam_time': course.exam_time,
        'exam_room': course.exam_room,
        'prerequisite': course.prerequisite
    }
    if isinstance(course, Practical_course):
        data['required_software'] = course.required_software
        data['equipment_fee'] = course.equipment_fee
    return data


def student_to_dict(student):
    courses = []
    for course, grade in student.courses.items():
        courses.append({
            'course_id': course.id,
            'grade': grade
        })
    return {
        'id': student.id,
        'name': student.name,
        'study_feild': student.study_feild,
        'faculty': student.faculty,
        'courses': courses
    }


def save_system(system):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    data = {
        'next_course_id': Course.next_id,
        'next_student_id': Student.next_id,
        'courses': [],
        'students': []
    }
    for course in system.courses:
        data['courses'].append(course_to_dict(course))
    for student in system.students:
        data['students'].append(student_to_dict(student))
    with DATA_FILE.open('w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def load_system():
    if not DATA_FILE.exists():
        return Management_system()

    try:
        with DATA_FILE.open('r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print('Data file is not valid JSON. A new empty system is loaded.')
        return Management_system()

    courses = set()
    students = set()
    courses_by_id = {}

    for course_data in data.get('courses', []):
        course = dict_to_course(course_data)
        courses.add(course)
        courses_by_id[course.id] = course

    for student_data in data.get('students', []):
        student = dict_to_student(student_data, courses_by_id)
        students.add(student)

    Course.next_id = max(data.get('next_course_id', 1), max_id(courses) + 1)
    Student.next_id = max(data.get('next_student_id', 1), max_id(students) + 1)

    return Management_system(students, courses)


def max_id(values):
    biggest = 0
    for value in values:
        if value.id > biggest:
            biggest = value.id
    return biggest


def dict_to_course(data):
    class_name = data['class_name']
    if class_name == 'Practical_course':
        course = Practical_course(
            data['name'],
            data['teacher'],
            data['department'],
            data['course_type'],
            data['units'],
            data['class_times'],
            data['class_room'],
            data['exam_time'],
            data['exam_room'],
            data['prerequisite'],
            data.get('required_software', []),
            data.get('equipment_fee', 0)
        )
    elif class_name == 'Theoretical_course':
        course = Theoretical_course(
            data['name'],
            data['teacher'],
            data['department'],
            data['course_type'],
            data['units'],
            data['class_times'],
            data['class_room'],
            data['exam_time'],
            data['exam_room'],
            data['prerequisite']
        )
    elif class_name == 'Presentation_course':
        course = Presentation_course(
            data['teacher'],
            data['units'],
            data['course_type']
        )
    else:
        raise ValueError('Unknown course class')
    course.id = data['id']
    return course


def dict_to_student(data, courses_by_id):
    student = Student(data['name'], data['study_feild'], data['faculty'])
    student.id = data['id']
    for item in data.get('courses', []):
        course = courses_by_id.get(item['course_id'])
        if course is not None:
            grade = item['grade']
            if grade is not None:
                grade = float(grade)
            student.add_course(course, grade)
    return student


def input_required(message):
    while True:
        value = input(message).strip()
        if value != '':
            return value
        print('This value is required.')


def input_default(message, default):
    value = input(f'{message} [{default}]: ').strip()
    if value == '':
        return default
    return value


def input_int(message, default=None):
    while True:
        if default is None:
            value = input(message).strip()
        else:
            value = input(f'{message} [{default}]: ').strip()
            if value == '':
                return default
        try:
            return int(value)
        except ValueError:
            print('Please enter an integer number.')


def input_float_or_none(message):
    while True:
        value = input(message).strip()
        if value == '':
            return None
        try:
            return float(value)
        except ValueError:
            print('Please enter a float number or leave it empty.')


def input_list(message):
    value = input(message).strip()
    if value == '':
        return []
    result = []
    for item in value.split(','):
        item = item.strip()
        if item != '':
            result.append(item)
    return result


def input_class_times():
    class_times = []
    count = input_int('How many class times? ', 0)
    for i in range(count):
        print(f'Class time {i + 1}')
        day = input_required('Day: ')
        time = input_required('Time (HH:MM - HH:MM): ')
        class_times.append({'day': day, 'time': time})
    return class_times


def input_exam_time():
    day = input_default('Exam day', '1405/01/01')
    time = input_default('Exam time', '00:00')
    return {'day': day, 'time': time}


def find_student(system, student_id):
    for student in system.students:
        if student.id == student_id:
            return student
    raise ValueError('Student not found')


def find_course(system, course_id):
    for course in system.courses:
        if course.id == course_id:
            return course
    raise ValueError('Course not found')


def format_average(average):
    if average is None:
        return 'None'
    return f'{average:.2f}'


def print_help():
    print()
    print('Commands:')
    print('  help                         Show this help')
    print('  add-student                  Add a new student')
    print('  list-students                Show students')
    print('  remove-student [student_id]  Remove a student')
    print('  add-course                   Add a new course')
    print('  list-courses                 Show courses')
    print('  remove-course [course_id]    Remove a course')
    print('  add-course-to-student        Add a course to a student')
    print('  add-grade                    Add or update a student grade')
    print('  student-courses [student_id] Show courses of one student')
    print('  sort-students average desc   Sort by average, name, or units')
    print('  stats                        Show grades statistics')
    print('  status [student_id]          Show passed or failed')
    print('  save                         Save data manually')
    print('  exit                         Save and exit')
    print()


def data_file_label():
    try:
        return str(DATA_FILE.relative_to(Path(__file__).parent))
    except ValueError:
        return DATA_FILE.name


def add_student_command(system):
    name = input_required('Name: ')
    study_feild = input_required('Study field: ')
    faculty = input_required('Faculty: ')
    student = Student(name, study_feild, faculty)
    system.add_student(student)
    print(f'Student added with id {student.id}.')


def list_students_command(system):
    if len(system.students) == 0:
        print('No students.')
        return
    for student in system.students:
        units = system.student_units(student)
        print(f'{student.id} - {student.name} - {student.study_feild} - {student.faculty} - average: {format_average(student.average)} - units: {units}')


def remove_student_command(system, parts):
    if len(parts) >= 2:
        student_id = int(parts[1])
    else:
        student_id = input_int('Student id: ')
    student = find_student(system, student_id)
    system.remove_student(student)
    print('Student removed.')


def add_course_command(system):
    print('Course classes: theoretical, practical, presentation')
    class_name = input_required('Course class: ').lower()
    if class_name == 'presentation':
        teacher = input_required('Teacher: ')
        units = input_int('Units: ')
        course_type = input_default('Course type (seminar/project)', 'seminar')
        course = Presentation_course(teacher, units, course_type)
    elif class_name == 'theoretical':
        course = input_theoretical_course()
    elif class_name == 'practical':
        course = input_practical_course()
    else:
        raise ValueError('Invalid course class')
    system.add_course(course)
    print(f'Course added with id {course.id}.')


def input_base_course_fields(course_types):
    print(f'Course types: {", ".join(course_types)}')
    name = input_required('Name: ')
    teacher = input_required('Teacher: ')
    department = input_required('Department: ')
    course_type = input_required('Course type: ')
    units = input_int('Units: ')
    class_times = input_class_times()
    class_room = input_default('Class room', 'default')
    exam_time = input_exam_time()
    exam_room = input_default('Exam room', 'default')
    prerequisite = input_list('Prerequisite course ids or names, separated by comma: ')
    return name, teacher, department, course_type, units, class_times, class_room, exam_time, exam_room, prerequisite


def input_theoretical_course():
    values = input_base_course_fields(Theoretical_course.course_types)
    return Theoretical_course(*values)


def input_practical_course():
    values = input_base_course_fields(Practical_course.course_types)
    required_software = input_list('Required software, separated by comma: ')
    equipment_fee = input_int('Equipment fee: ', 0)
    return Practical_course(*values, required_software, equipment_fee)


def list_courses_command(system):
    if len(system.courses) == 0:
        print('No courses.')
        return
    for course in system.courses:
        print(f'{course.id} - {course.__class__.__name__} - {course.name} - {course.teacher} - {course.course_type} - units: {course.units}')


def remove_course_command(system, parts):
    if len(parts) >= 2:
        course_id = int(parts[1])
    else:
        course_id = input_int('Course id: ')
    course = find_course(system, course_id)
    system.remove_course(course)
    print('Course removed.')


def add_course_to_student_command(system):
    student_id = input_int('Student id: ')
    course_id = input_int('Course id: ')
    grade = input_float_or_none('Grade, empty for no grade: ')
    student = find_student(system, student_id)
    course = find_course(system, course_id)
    system.add_course_to_student(student, course, grade)
    print('Course added to student.')


def add_grade_command(system):
    student_id = input_int('Student id: ')
    course_id = input_int('Course id: ')
    grade = input_float_or_none('Grade: ')
    if grade is None:
        raise ValueError('Grade is required')
    student = find_student(system, student_id)
    course = find_course(system, course_id)
    system.add_grade_to_student(student, course, grade)
    print('Grade saved.')


def student_courses_command(system, parts):
    if len(parts) >= 2:
        student_id = int(parts[1])
    else:
        student_id = input_int('Student id: ')
    student = find_student(system, student_id)
    if len(student.courses) == 0:
        print('This student has no courses.')
        return
    for course, grade in student.courses.items():
        print(f'{course.id} - {course.name} - units: {course.units} - grade: {grade}')


def sort_students_command(system, parts):
    if len(parts) < 2:
        print('Usage: sort-students average|name|units [asc|desc]')
        return
    reverse = len(parts) >= 3 and parts[2].lower() == 'desc'
    key = parts[1].lower()
    if key == 'average':
        students = system.sort_students_by_average(reverse)
    elif key == 'name':
        students = system.sort_students_by_name(reverse)
    elif key == 'units':
        students = system.sort_students_by_units(reverse)
    else:
        raise ValueError('Invalid sort key')
    for student in students:
        units = system.student_units(student)
        print(f'{student.id} - {student.name} - average: {format_average(student.average)} - units: {units}')


def stats_command(system):
    print(f'Average: {system.grades_average()}')
    print(f'Standard deviation: {system.grades_standard_deviation()}')
    print(f'Max grade: {system.max_grade()}')
    print(f'Min grade: {system.min_grade()}')


def status_command(system, parts):
    if len(parts) >= 2:
        student_id = int(parts[1])
    else:
        student_id = input_int('Student id: ')
    student = find_student(system, student_id)
    print(f'{student.name}: {system.student_status(student)}')


def command_needs_save(command):
    return command in {
        'add-student',
        'remove-student',
        'add-course',
        'remove-course',
        'add-course-to-student',
        'add-grade'
    }


def run_command(system, parts):
    command = parts[0].lower()
    if command == 'help':
        print_help()
    elif command == 'add-student':
        add_student_command(system)
    elif command == 'list-students':
        list_students_command(system)
    elif command == 'remove-student':
        remove_student_command(system, parts)
    elif command == 'add-course':
        add_course_command(system)
    elif command == 'list-courses':
        list_courses_command(system)
    elif command == 'remove-course':
        remove_course_command(system, parts)
    elif command == 'add-course-to-student':
        add_course_to_student_command(system)
    elif command == 'add-grade':
        add_grade_command(system)
    elif command == 'student-courses':
        student_courses_command(system, parts)
    elif command == 'sort-students':
        sort_students_command(system, parts)
    elif command == 'stats':
        stats_command(system)
    elif command == 'status':
        status_command(system, parts)
    elif command == 'save':
        save_system(system)
        print('Data saved.')
    else:
        print('Unknown command. Type help to see commands.')


def main():
    system = load_system()
    print('Educational management system')
    print(f'Data file: {data_file_label()}')
    print('Type help to see commands.')
    print('Changes are saved automatically after each successful change.')

    while True:
        try:
            command_line = input('edu> ').strip()
        except EOFError:
            save_system(system)
            print('Data saved. Goodbye.')
            break
        if command_line == '':
            continue
        parts = command_line.split()
        command = parts[0].lower()
        if command in ('exit', 'quit'):
            save_system(system)
            print('Data saved. Goodbye.')
            break
        try:
            run_command(system, parts)
            if command_needs_save(command):
                save_system(system)
                print('Data saved.')
        except (ValueError, TypeError) as error:
            print(f'Error: {error}')


if __name__ == '__main__':
    main()
