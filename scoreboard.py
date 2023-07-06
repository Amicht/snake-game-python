from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')


class ScoreBoard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.score = 0
        self.height = int((screen_height / 2) - 30)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, self.height)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
