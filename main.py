"""
The main is responsible for invocation of the robot with the commands
Input: File with the commands e.g. commands_1.txt
Output: Robot object
Sample Invocation: python main.py input/commands_1.txt
"""

import sys
from utils import readFile,preprocessCommands
from robot import Robot
from direction import Direction
from grid import Grid


def main():
    if len(sys.argv) != 2:
        "please pass the file of the commands"
        exit(0)


    Commands = readFile(sys.argv[1])
    orientations = ["NORTH", "EAST", "SOUTH", "WEST"]


    grid = Grid()
    robot = Robot(orientations=orientations)


    if "PLACE" not in Commands[0]:
        print("The first valid command to the robot is a PLACE command, please specify it")


    elif "PLACE" in Commands[0]:
            for command in Commands:
                if "PLACE" in command:
                    command_splitted = preprocessCommands(command)
                    x_axis = float(command_splitted[0])
                    y_axis = float(command_splitted[1])
                    facing = command_splitted[2]
                    orientations_index = orientations.index(facing)
                    robot_position = Direction(x_axis=x_axis, y_axis=y_axis)
                    robot = robot.place(Direction=robot_position,grid=grid,facing=orientations_index/2.0)
                else:
                    robot = getattr(robot,command.lower())()

if __name__ == "__main__":
 main()