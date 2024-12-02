from turtle import Turtle, register_shape
import random

STEP_WIDTH = 10
CACTUS_GIF = 'resources/cactus.gif'
register_shape(CACTUS_GIF)


class Cactus(Turtle):
    def __init__(self, x, y):
        # super().__init__()
        self.cactus = Turtle(CACTUS_GIF)
        self.cactus.penup()
        self.cactus.teleport(x, y)
        self.cactus.setheading(180)
        self.cactus.speed('fastest')

    def add(self):
        pass

    def move(self):
        """Though a cactus normally doesn't move, it seems so - as the T-Rex is in focus and seems to be static."""
        self.cactus.forward(STEP_WIDTH)
