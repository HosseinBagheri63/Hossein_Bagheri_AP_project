class SimpleFraction(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator == 0:
            raise ValueError('Denominator cannot be zero')
        self.denominator = denominator
    def __str__(self):
        return str(self.numerator / self.denominator)
    def times(self, other):
        return SimpleFraction(self.numerator * other.numerator, self.denominator * other.denominator)
    def plus(self, other):
        return SimpleFraction(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator)
    def get_inverse(self):
        return SimpleFraction(self.denominator, self.numerator)
    def invert(self):
        self.numerator, self.denominator = self.denominator, self.numerator

class Student:
    def __init__(self,name:str,grade:int):
        self.name=name
        self.__grade=grade
    @property
    def getGrade(self) -> int:
        return self.__grade
    
    def setGreade(self)
        
ali= Student("ali", 2)
print(ali.getGrade)