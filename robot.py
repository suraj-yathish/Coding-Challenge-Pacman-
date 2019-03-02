
from math import pi,sin,cos

from direction import Direction

class Robot(object):

    def __init__(self, direction = Direction(0.0, 0.0), facing = 0.0, board = None, orientations=None):
        """Constructor of the toy robot, takes 2 mandatory and 2 optional parameters"""
        self.position = direction
        self.facing = facing
        self.board = board
        self.orientations = orientations



    def left(self):
        """Move the toy robot 90 degrees to the left"""
        return self.place(self.position, (self.facing - 0.5)%2, self.board)

    def right(self):
        """Move the toy robot 90 degrees to the right"""
        return self.place(self.position, (self.facing + 0.5)%2, self.board)

    def move(self):
        """Move the toy robot one unit forward in the direction it is currently facing"""
        return self.place(self.position + Direction(sin(pi * self.facing),cos(pi * self.facing)),self.facing, self.board)

    def report(self):
        """Announce the X,Y and F of the robot and prints the result"""
        if self.board is not None:
            print(round(self.position.x_axis), round(self.position.y_axis), self.orientations[round(self.facing*2)])
        return self

    def place(self, position, facing, board):
        """Put the toy robot on the table in position X,Y and facing to orientations like North, South, East or West"""
        if board is not None and board.onSurface(position):
            return Robot(position, facing, board, self.orientations)
        else:
         return self