"""
This main function invokes pacman with the commands

Input: File with the commands e.g. test_command_1.txt
Output: Pacman object
How to Invoke: python main.py input/test_command_1.txt
"""

import sys
from utils import readFile,preprocessCommands
from pacman import Pacman
from direction import Direction
from grid import Grid


def main():
    if len(sys.argv) != 2:
        "please pass the file of the commands"
        exit(0)


    Commands = readFile(sys.argv[1])
    orientations = ["NORTH", "EAST", "SOUTH", "WEST"]


    grid = Grid()
    pacman = Pacman(orientations=orientations)


    if "PLACE" not in Commands[0]:
        print("The first valid command to the pacman is a PLACE command, please specify it")


    elif "PLACE" in Commands[0]:
            for command in Commands:
                if "PLACE" in command:
                    command_splitted = preprocessCommands(command)
                    x_axis = float(command_splitted[0])
                    y_axis = float(command_splitted[1])
                    facing = command_splitted[2]
                    orientations_index = orientations.index(facing)
                    pacman_position = Direction(x_axis=x_axis, y_axis=y_axis)
                    pacman = pacman.place(Direction=pacman_position,grid=grid,facing=orientations_index/2.0)
                else:
                    pacman = getattr(pacman,command.lower())()

if __name__ == "__main__":
 main()