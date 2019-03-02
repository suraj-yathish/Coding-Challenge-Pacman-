import unittest
from pacman import Pacman
from grid import Grid
from direction import Direction

grid = Grid()
orientations = ["NORTH", "EAST", "SOUTH", "WEST"]

class TestPacman(unittest.TestCase):

        def test_left(self):
            test_pacman_1 = Pacman(direction=Direction(0.0, 0.0), facing=0.0, grid=grid, orientations=orientations)
            result_pacman_1 = Pacman(direction=Direction(0.0, 0.0), facing=1.5, grid=grid, orientations=orientations)

            test_pacman_2 = Pacman(direction=Direction(0.0, 0.0),  facing=1.0, grid=grid, orientations=orientations)
            result_pacman_2 = Pacman(direction=Direction(0.0, 0.0), facing=2.5, grid=grid, orientations=orientations)

            test_pacman_1.__eq__(result_pacman_1)
            test_pacman_2.__eq__(result_pacman_2)


        def test_right(self):
            test_pacman_1 = Pacman(direction=Direction(0.0, 0.0), facing=1.5, grid=grid, orientations=orientations)
            result_pacman_1 = Pacman(direction=Direction(0.0, 0.0), facing=0.0, grid=grid, orientations=orientations)

            test_pacman_2 = Pacman(direction=Direction(0.0, 0.0), facing=2.5, grid=grid, orientations=orientations)
            result_pacman_2 = Pacman(direction=Direction(0.0, 0.0), facing=1.0, grid=grid, orientations=orientations)

            test_pacman_1.__eq__(result_pacman_1)
            test_pacman_2.__eq__(result_pacman_2)

        def test_move(self):
            test_pacman = Pacman(direction= Direction(0.0,0.0), facing=0.0, grid=grid, orientations=orientations)
            test_pacman = test_pacman.move()
            result_pacman = Pacman(direction= Direction(0.0,1.0), facing=0.0, grid=grid, orientations=orientations)
            test_pacman.__eq__(result_pacman)


        def test_place(self):
            test_pacman = Pacman()
            result_pacman = Pacman(direction= Direction(1.0,2.0), facing=0.5, grid=grid, orientations=orientations)
            test_pacman = test_pacman.place(direction= Direction(0.0,0.0), facing=0.0, grid=grid)
            test_pacman.__eq__(result_pacman)

        if __name__ == '__main__':

           unittest.main()