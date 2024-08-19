from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = Scoreboard()

right = []
left = []
ans = "yes"
game_on = False

while ans == "yes":

    match = screen.textinput("Match", "How many points to win?")
    if match:
        game_on = True
    while game_on:

        screen.listen()
        screen.onkey(l_paddle.up, "w")
        screen.onkey(l_paddle.down, "s")
        screen.onkey(r_paddle.up, "Up")
        screen.onkey(r_paddle.down, "Down")

        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (
                ball.distance(l_paddle) < 50 and ball.xcor() < -320):
            ball.rebound()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()
        if ball.xcor() < -380 or ball.xcor() > 380:

            if ball.xcor() < -380:
                ball.reset_pos()
                score.r_increase()
                right.append(score.r_score)
                if right[-1] == int(match):
                    score.game_over()
                    screen.update()
                    time.sleep(1)
                    game_on = False

            else:
                score.l_increase()
                ball.reset_pos()
                left.append(score.l_score)

                if left[-1] == int(match):
                    score.game_over()
                    screen.update()
                    time.sleep(1)
                    game_on = False
    ans = screen.textinput("New game?", "Do you want to play again?")

    score.new_game()

screen.exitonclick()
