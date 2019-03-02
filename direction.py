class Direction(object):

    def __init__(self, x_axis, y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def __add__(self, other):
        return Direction(self.x_axis + other.x_axis, self.y_axis + other.y_axis)

    def __ge__(self, other):
        return self.x_axis >= other.x_axis and self.y_axis >= other.y_axis

    def __le__(self, other):
        return self.x_axis <= other.x_axis and self.y_axis <= other.y_axis

