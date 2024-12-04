from turtle import Turtle, register_shape
from enum import Enum

HERO_GIF = 'resources/t-rex.gif'
JUMP_HEIGHT = 350
STEP_WIDTH_UP = 50
STEP_WIDTH_DOWN = 50

# registering the image as a new shape
register_shape(HERO_GIF)


class JumpState(Enum):
    WAIT_FOR_TRIGGER = 0
    ASCENDING = 1
    TURNING = 2
    DESCENDING = 3
    RETURNED_TO_FLOOR = 4


class Hero:
    def __init__(self, x, y):
        self.hero_turtle = Turtle(HERO_GIF)
        self.hero_turtle.penup()
        self.hero_turtle.speed('fastest')
        self.hero_turtle.teleport(x, y)
        self.state = JumpState.WAIT_FOR_TRIGGER

    def jump_ascend(self, floor_ycor):
        self.hero_turtle.setheading(90)  # up
        if self.hero_turtle.ycor() > floor_ycor + JUMP_HEIGHT:
            self.hero_turtle.sety(floor_ycor + JUMP_HEIGHT)
        else:
            self.hero_turtle.forward(STEP_WIDTH_UP)

    def jump_descend(self, floor_ycor):
        self.hero_turtle.setheading(270)  # down
        if self.hero_turtle.ycor() > floor_ycor:
            self.hero_turtle.forward(STEP_WIDTH_DOWN)

    def get_jump_state(self, floor_ycor) -> JumpState:
        if self.state == JumpState.RETURNED_TO_FLOOR:
            self.state = JumpState.WAIT_FOR_TRIGGER
        elif self.hero_turtle.ycor() <= floor_ycor:
            if self.hero_turtle.heading() == 270.0:
                self.hero_turtle.sety(floor_ycor)
                self.hero_turtle.setheading(90.0)  # turn to head upwards
                self.state = JumpState.RETURNED_TO_FLOOR
            else:
                self.state = JumpState.WAIT_FOR_TRIGGER
        elif self.hero_turtle.ycor() >= floor_ycor + JUMP_HEIGHT:
            self.state = JumpState.TURNING
        elif self.hero_turtle.heading() == 90.0:
            self.state = JumpState.ASCENDING
        else:
            self.state = JumpState.DESCENDING

        return self.state
