class Coordinate(object):
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

class Circle ():
    def __init__(self, center, radius: float):
        if not (isinstance(center, Coordinate)):
            raise ValueError ('center should be a coordinate')
        if not (isinstance(radius, float)):
            raise ValueError ('center should be a float')
        self.center= center
        self.radius= radius