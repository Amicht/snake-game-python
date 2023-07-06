import time
from turtle import Turtle, Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game - Python")
screen.tracer(n=0)

snake = Snake()
food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
scoreboard = ScoreBoard(SCREEN_HEIGHT)

screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()


def check_wall_collision():
    x_boundry = int(SCREEN_WIDTH / 2)
    y_boundry = int(SCREEN_HEIGHT / 2)
    snake_x = snake.head.xcor()
    snake_y = snake.head.ycor()
    if snake_x >= x_boundry or snake_x <= -1 * x_boundry or snake_y >= y_boundry or snake_y <= -1 * y_boundry:
        return True
    return False


def check_tail_collision():
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            return True
    return False


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect wall collision:
    if check_wall_collision() or check_tail_collision():
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
