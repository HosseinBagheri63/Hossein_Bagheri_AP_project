from abc import ABC , abstractmethod
import re
class Course(ABC):
    course_types=[]
    def __init__(self, name:str, teacher:str, department:str, course_type:str, id:str, units:int, class_times:list, class_room:str, exam_time:dict, exam_room:str, prerequisite:list):
        self.name = name
        self.teacher = teacher
        self.department = department
        self.course_type = course_type
        self.id = id
        self.units = units
        self.class_times = class_times
        self.class_room = class_room
        self.exam_time = exam_time
        self.exam_room = exam_room
        self.prerequisite = prerequisite
    @property
    def class_times(self):
        return self._class_times
    
    @class_times.setter
    def class_times(self, value):
        class_time_pattern= r"(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]) - (0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])"

        for day in value:
            if type(day) is not dict:
                raise TypeError('Class times must be a list of dictionaries')
            if 'day' not in day or 'time' not in day:
                raise ValueError('Class times must be a list of dictionaries with keys "day", "time"')
            if day['day'] not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                raise ValueError('Day must be one of "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" or "Sunday"')
            if re.fullmatch(class_time_pattern, day['time']) is None:
                raise ValueError('Time must be in the format "HH:MM - HH:MM"')
        self._class_times = value

    @property
    def exam_time(self):
        return self._exam_time
    
    @exam_time.setter
    def exam_time(self, value):
        exam_time_pattern = r"(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])"
        exam_day_pattern = r"(1[4-9][0-9][5-9])/(0[1-9]|1[0-2])/([0-2][1-9]|3[0-1])"
        if 'day' not in value or 'time' not in value:
            raise ValueError('Exam time must be a dictionary with keys "day", "time"')
        if re.fullmatch(exam_time_pattern, value['time']) is None or re.fullmatch(exam_day_pattern, value['day']) is None:
            raise ValueError('Exam time must be in the format "HH:MM"')
        
        self._exam_time = value
    
    @property
    def course_type(self):
        return self._course_type
    
    @course_type.setter
    def course_type(self, value):
        if value not in self.course_types:
            raise ValueError()
        self._course_type = value

    @abstractmethod
    def __str__(self):
        pass


    def __eq__(self, value) -> bool:
        return self.id==value.id

    def __hash__(self):
        return hash(self.id)

class Practical_course(Course):
    course_types = ['workshop', 'Laboratory','workshop_optional', 'Laboratory_optional' ]
    def __init__(self, name:str, teacher:str, department:str, course_type:str, id:str, units:int, class_times:list, class_room:str, exam_time:dict, exam_room:str, prerequisite:list, required_software:list, equipment_fee:int):
        super().__init__(name, teacher, department, course_type, id, units, class_times, class_room, exam_time, exam_room, prerequisite)
        self.required_software = required_software
        self.equipment_fee = equipment_fee

    def __str__(self):
        return f"Course: {self.name} - {self.id} - {self.teacher} - {self.department} - {self.course_type} - {self.units} - {self.class_times} - {self.class_room} - {self.exam_time} - {self.exam_room} - {self.required_software} - {self.equipment_fee}"

    

class Theoretical_course(Course):
    course_types = ['base', 'Specialized', 'Specialized_optional', 'optional', 'general']
    def __str__(self):
        return f"Course: {self.name} - {self.id} - {self.teacher} - {self.department} - {self.course_type} - {self.units} - {self.class_times} - {self.class_room} - {self.exam_time} - {self.exam_room} - {self.prerequisite}"


class Presentation_course(Course):
    course_types = ['seminar', 'project']
    def __init__(self, id:str, teacher:str, units:int, course_type:str='seminar'):
        super().__init__('presentation', teacher, 'default', course_type, id, units, [], 'default', {'day':'1405/01/01', 'time':'00:00'}, 'default', [])

    def __str__(self):
        return f"Course: {self.id} - {self.teacher} - {self.units}"

