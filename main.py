from turtle import Screen, Turtle
from hero import Hero
from cactus import Cactus
from scoreboard import Scoreboard
from random import randint
import pyautogui

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
Y_FLOOR = -150
Y_MOVING_BASE = Y_FLOOR - 20  # The bottom line of all objects
DELAY = 100  # milliseconds

jump_triggered = False
bot_active = False
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("My Dinosaur Game")
screen.bgcolor('white')
screen.clearscreen()


def draw_line(color):
    line = Turtle()
    line.hideturtle()
    line.color(color)
    line.pensize(5)
    line.teleport(x=SCREEN_WIDTH / -2, y=Y_FLOOR)
    line.setheading(0)
    line.pendown()
    line.speed('fastest')
    line.goto((SCREEN_WIDTH / 2, Y_FLOOR))


draw_line('black')
dino = Hero(SCREEN_WIDTH / -2 + 150, Y_MOVING_BASE)
cactus = Cactus(350, Y_MOVING_BASE)
scoreboard = Scoreboard()


def jump():
    """Key-Press triggered routine.
    The dino jump is divided into four phases: inactive, move-up, turn, move-down.
    """
    global jump_triggered
    if jump_triggered == False:
        return

    state = dino.get_jump_state(Y_MOVING_BASE)
    if state == 0 or state == 1:  # inactive or ascending
        dino.jump_ascend(Y_MOVING_BASE)
    elif state == 4:  # returned to floor
        dino.reinit_jump_state()
    elif state == 5:  # wait one cycle
        jump_triggered = False
    else:  # turning or descending
        dino.jump_descend(Y_MOVING_BASE)

    screen.ontimer(jump, DELAY)


def jump_key_pressed():
    global jump_triggered
    if jump_triggered == False:
        jump_triggered = True
        jump()


def activate_bot():
    global bot_active
    if bot_active == False:
        bot_active = True
        print("Game is controlled by bot.")
    else:
        bot_active = False
        print("Game botis deactivated.")


# reacting upon keys
screen.listen()
screen.onkey(jump_key_pressed, 'space')
screen.onkey(activate_bot, 'b')


def main():
    global bot_active
    game_is_on = True
    while game_is_on:
        cactus.move()
        screen.update()

        if bot_active:
            if dino.hero_turtle.distance(cactus.cactus) < 250.0:
                pyautogui.press('space')

        # detect cactus-passed event
        if cactus.cactus.xcor() < SCREEN_WIDTH / -2 + 20:
            scoreboard.increase_score()
            cactus.cactus.teleport(
                x=SCREEN_WIDTH / 2 + randint(-200, 300), y=Y_MOVING_BASE)

        # detect collision with cactus
        if dino.hero_turtle.distance(cactus.cactus) < 50.0:
            scoreboard.game_over()
            game_is_on = False

    screen.exitonclick()


if __name__ == '__main__':
    main()
