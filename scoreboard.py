from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')


class ScoreBoard(Turtle):
    def __init__(self, screen_height):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.height = int((screen_height / 2) - 30)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, self.height)
        self.get_highest_score()
        self.show_score()

    def get_highest_score(self):
        with open("high_score.txt", mode="r") as file:
            high_score = file.read()
            if not high_score:
                self.update_highest_score(0)
            else:
                self.high_score = int(high_score)

    def update_highest_score(self, high_score):
        with open("high_score.txt", mode="w") as file:
            file.write(str(high_score))
        self.high_score = high_score

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.show_score()

    def reset(self):
        if self.score > self.high_score:
            self.update_highest_score(self.score)
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over.", align=ALIGNMENT, font=FONT)
