class Employee(object):
    _number_of_employees = 0
    def __init__(self, name:str, ID:str, salary:int):
        self.name = name
        self.ID = ID
        self._salary = salary
        Employee._number_of_employees += 1
    @classmethod
    def number_of_employees(cls):
        return cls._number_of_employees
    @property
    def ID(self):
        return self._ID
    @ID.setter
    def ID(self, value):
        if (value[0].isdigit()==False) and len(value) == 4 and value[1:4].isdigit():
            self._ID = value
        else:
            raise ValueError("Invalid ID")
    @property
    def salary(self):
        return self._salary
class Manager(Employee):
    _number_of_managers = 0
    def __init__(self, name:str, ID:str):
        super().__init__(name, ID, 4000)
        Manager._number_of_managers += 1
    @classmethod
    def number_of_managers(cls):
        return cls._number_of_managers
    @property
    def ID(self):
        return self._ID
    @ID.setter
    def ID(self, value):
        if value.startswith("M")and len(value) == 4 and value[1:4].isdigit():
            self._ID = value
        else:
            raise ValueError("Invalid ID")
    @staticmethod
    def Manager_ID_validation(value):
        if value.startswith("M")and len(value) == 4 and value[1:4].isdigit():
            return True
        else:
            return False
class Developer(Employee):
    _number_of_developers = 0
    def __init__(self, name:str, ID:str, working_hours:int=160, salary_per_hour:int=25):
        super().__init__(name, ID, salary_per_hour*working_hours)
        self._working_hours = working_hours
        self._salary_per_hour = salary_per_hour
        Developer._number_of_developers += 1
    @property
    def working_hours(self):
        return self._working_hours
    @working_hours.setter
    def working_hours(self, value):
        if value > 0 and value < 576:
            self._working_hours = value
        else:
            raise ValueError("Invalid working hours")
    @property
    def salary_per_hour(self):
        return self._salary_per_hour
    @salary_per_hour.setter
    def salary_per_hour(self, value):
        if value > 0:
            self._salary_per_hour = value
        else:
            raise ValueError("Invalid salary per hour")
    @classmethod
    def number_of_developers(cls):
        return cls._number_of_developers
    @property
    def ID(self):
        return self._ID
    @ID.setter
    def ID(self, value):
        if value.startswith("D")and len(value) == 4 and value[1:4].isdigit():
            self._ID = value
        else:
            raise ValueError("Invalid ID")
    @staticmethod
    def Developer_ID_validation(value):
        if value.startswith("D")and len(value) == 4 and value[1:4].isdigit():
            return True
        else:
            return False
manager = Manager("Reza", "M123")
developer = Developer("Ali", "D123")
print(Manager.number_of_managers())
print(Developer.number_of_developers())
print(Employee.number_of_employees())
print(manager.ID)
print(manager.salary)
print(manager.name)
print(developer.ID)
print(developer.salary)
print(developer.name)
developer2 = Developer("Ali", "D1234")
print(developer2.ID)
print(developer2.salary)
print(developer2.name)
