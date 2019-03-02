
from math import pi,sin,cos

from direction import Direction

class Pacman(object):

    def __init__(self, direction = Direction(0.0, 0.0), facing = 0.0, grid = None, orientations=None):
        """Constructor for the pacman, takes 2 mandatory and 2 optional parameters"""
        self.direction = direction
        self.facing = facing
        self.grid = grid
        self.orientations = orientations



    def left(self):
        """Move pacman 90 degrees to the left"""
        return self.place(self.direction, (self.facing - 0.5)%2, self.grid)

    def right(self):
        """Move pacman 90 degrees to the right"""
        return self.place(self.direction, (self.facing + 0.5)%2, self.grid)

    def move(self):
        """Move pacman one unit forward in the direction it is currently facing"""
        return self.place(self.direction + Direction(sin(pi * self.facing),cos(pi * self.facing)),self.facing, self.grid)

    def report(self):
        """Announce the X,Y and F of the pacman and prints the result"""
        if self.grid is not None:
            print(round(self.direction.x_axis), round(self.direction.y_axis), self.orientations[round(self.facing*2)])
        return self

    def place(self, direction, facing, grid):
        """Put the pacman on the table in position X,Y and facing to orientations like North, South, East or West"""
        if grid is not None and grid.onGridSurface(direction):
            return Pacman(direction, facing, grid, self.orientations)
        else:
         return self