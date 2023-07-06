from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self, screen_w, screen_h):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.half_w = int((screen_w / 2) - 20)
        self.half_h = int((screen_h / 2) - 20)
        self.refresh()

    def refresh(self):
        rand_x = random.randint(self.half_w*-1, self.half_w)
        rand_y = random.randint(self.half_h*-1, self.half_h)
        self.goto(rand_x, rand_y)