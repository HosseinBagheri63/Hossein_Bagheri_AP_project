import math
class Circle():

    def __init__(self, radius):
    # initilizes self with radius
        self._radius= radius

    @property
    def radius(self):
    # returns radius of self
        return self._radius

    @radius.setter
    def radius(self, radius):
    # changes the radius attribute of self to radius
        if radius > 0:   #radius cant be smaller than 0
            self._radius= radius
        else:
            raise ValueError("radius must be positive")

    def area(self):
    # computes and returns area of self
        return math.pi * self._radius ** 2

    def __eq__(self, other):
    # other is a Circle object
    # returns True if self and other has the same radius value
        return self._radius == other._radius

    def __gt__(self, other):
    # other is a Circle object
    # returns self or other, Circle object with the bigger radius
        if self._radius == other._radius:
            return None
        return self if self._radius > other._radius else other

    def __add__(self, other):
    # other is a Circle object
    # returns a new Circle object that it's radius is
    # the sum of self and other's radius
        return Circle(self._radius + other._radius)

    def __str__(self):
    # a Circle's string reperesentation is the radius
        return str(self._radius)