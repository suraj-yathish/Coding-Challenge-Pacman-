
class Grid(object):

    def __init__(self):
        self.x_low = 0.0
        self.x_high = 4.0
        self.y_low = 0.0
        self.y_high = 4.0

    def onGridSurface(self, direction):
     return self.x_low <= direction.x_axis <= self.x_high and self.y_low <= direction.y_axis and self.y_high >= direction.y_axis