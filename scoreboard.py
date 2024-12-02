from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color('black')
        self.speed('fastest')
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {
                   self.high_score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        if self.score > self.high_score:
            with open('data.txt', 'w') as data:
                data.write(f"{self.score}")
        self.home()
        self.write(f'Game Over!', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
