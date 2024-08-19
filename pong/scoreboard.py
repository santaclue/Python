from turtle import Turtle, Screen

screen = Screen()
ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 200)
        self.hideturtle()
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGN, font=("Comic Sans", 50, "normal"))
        self.update_scoreboard()

    #
    def update_scoreboard(self):
        self.write(f"{self.l_score} : {self.r_score}", align=ALIGN, font=("Comic Sans", 50, "normal"))

    def game_over(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=FONT)

    def new_game(self):

        self.clear()
        self.r_score=0
        self.l_score=0
        self.goto(0,200)
        self.update_scoreboard()

    def r_increase(self):
        self.clear()
        self.r_score += 1

        self.update_scoreboard()

    def l_increase(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()
