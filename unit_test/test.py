import unittest
from robot import Robot
from grid import Grid
from direction import Direction

grid = Grid()
orientations = ["NORTH", "EAST", "SOUTH", "WEST"]

class TestRobot(unittest.TestCase):

        def test_left(self):
            test_robot_1 = Robot(direction=Direction(0.0, 0.0), facing=0.0, board=grid, orientations=orientations)
            result_robot_1 = Robot(direction=Direction(0.0, 0.0), facing=1.5, board=grid, orientations=orientations)

            test_robot_2 = Robot(direction=Direction(0.0, 0.0),  facing=1.0, board=grid, orientations=orientations)
            result_robot_2 = Robot(direction=Direction(0.0, 0.0), facing=2.5, board=grid, orientations=orientations)

            test_robot_1.__eq__(result_robot_1)
            test_robot_2.__eq__(result_robot_2)


        def test_right(self):
            test_robot_1 = Robot(direction=Direction(0.0, 0.0), facing=1.5, board=grid, orientations=orientations)
            result_robot_1 = Robot(direction=Direction(0.0, 0.0), facing=0.0, board=grid, orientations=orientations)

            test_robot_2 = Robot(direction=Direction(0.0, 0.0), facing=2.5, board=grid, orientations=orientations)
            result_robot_2 = Robot(direction=Direction(0.0, 0.0), facing=1.0, board=grid, orientations=orientations)

            test_robot_1.__eq__(result_robot_1)
            test_robot_2.__eq__(result_robot_2)

        def test_move(self):
            test_robot = Robot(direction= Direction(0.0,0.0), facing=0.0, board=grid, orientations=orientations)
            test_robot = test_robot.move()
            result_robot = Robot(direction= Direction(0.0,1.0), facing=0.0, board=grid, orientations=orientations)
            test_robot.__eq__(result_robot)


        def test_place(self):
            test_robot = Robot()
            result_robot = Robot(direction= Direction(1.0,2.0), facing=0.5, board=grid, orientations=orientations)
            test_robot = test_robot.place(position=Direction(0.0,0.0), facing=0.0, board=grid)
            test_robot.__eq__(result_robot)

        if __name__ == '__main__':

           unittest.main()