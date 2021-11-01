from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor((239, 211, 160))
screen.title("Super Snake Game")
screen.tracer(0)


snake = Snake()
food = Food(screen)
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
is_increase_speed = False

speed = 0.09
next_lap = 10
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    if snake.head.distance(food) < 20:
        scoreboard.increase_score()
        food.refresh(screen)
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    if snake.is_crashed_tail():
        game_is_on = False
        scoreboard.game_over()

    if speed == 0.05 and scoreboard.score == next_lap:
        speed = 0.10

    if scoreboard.score == next_lap:
        speed -= 0.01
        next_lap += 10

screen.exitonclick()
