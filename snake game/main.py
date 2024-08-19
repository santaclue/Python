from turtle import Screen
import time
from snake import Snake
from food import Food
from Scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
screen.setup(600, 600, 0, 0)

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend_length()
        score.increase_score()

    for i in snake.segments[1:]:
        if snake.head.distance(i)<15:
            score.reset()
            snake.reset()




    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        score.reset()
        snake.reset()


    snake.move()
















screen.exitonclick()