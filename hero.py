from turtle import Turtle, register_shape

HERO_GIF = 'resources/t-rex.gif'
JUMP_HEIGHT = 350
STEP_WIDTH_UP = 50
STEP_WIDTH_DOWN = 50
JUMP_STATE_WAIT_FOR_TRIGGER = 0
JUMP_STATE_ASCENDING = 1
JUMP_STATE_TURNING = 2
JUMP_STATE_DESCENDING = 3
JUMP_STATE_RETURNED_TO_FLOOR = 4
JUMP_STATE_WAIT_ONE_CYCLE = 5

# registering the image as a new shape
register_shape(HERO_GIF)


class Hero:
    def __init__(self, x, y):
        # super().__init__()
        self.hero_turtle = Turtle(HERO_GIF)
        self.hero_turtle.penup()
        self.hero_turtle.speed('fastest')
        self.hero_turtle.teleport(x, y)
        self.state = JUMP_STATE_WAIT_FOR_TRIGGER

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

    def reinit_jump_state(self):
        self.hero_turtle.state = JUMP_STATE_WAIT_ONE_CYCLE

    def get_jump_state(self, floor_ycor):
        if self.state == JUMP_STATE_RETURNED_TO_FLOOR:
            self.state = JUMP_STATE_WAIT_ONE_CYCLE
        elif self.state == JUMP_STATE_WAIT_ONE_CYCLE:
            self.state = JUMP_STATE_WAIT_FOR_TRIGGER
        elif self.hero_turtle.ycor() <= floor_ycor:
            if self.hero_turtle.heading() == 270.0:
                self.hero_turtle.sety(floor_ycor)
                self.hero_turtle.setheading(90.0)  # turn to head upwards
                self.state = JUMP_STATE_RETURNED_TO_FLOOR
            else:
                self.state = JUMP_STATE_WAIT_FOR_TRIGGER
        elif self.hero_turtle.ycor() >= floor_ycor + JUMP_HEIGHT:
            self.state = JUMP_STATE_TURNING
        elif self.hero_turtle.heading() == 90.0:
            self.state = JUMP_STATE_ASCENDING
        else:
            self.state = JUMP_STATE_DESCENDING

        return self.state
