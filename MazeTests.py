from Maze import *
import random
import turtle
import unittest

class testMaze(unittest.TestCase):
    def setUp(self):
        
        # this checks for a Maze class
        self.m=Maze()

    def testMazeExists(self):

        pass

    def testScreenExists(self):
        assert type(self.m) == turtle._Screen

    def testTurtleExists(self):
        assert type(self.m.t) == turtle._Turtle


if __name__=="__main__":
    unittest.main(exit=False)

unittest.main()

