
class Grid(object):

    def __init__(self):
        self.x_low = 0.0
        self.x_high = 4.0
        self.y_low = 0.0
        self.y_high = 4.0

    def onSurface(self, position):
     return self.x_low <= position.x_axis <= self.x_high and self.y_low <= position.y_axis and self.y_high >= position.y_axis