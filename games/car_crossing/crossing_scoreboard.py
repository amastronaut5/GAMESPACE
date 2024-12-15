from turtle import Turtle
FONT = ("agency fb", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level= 1
        self.hideturtle()
        self.penup()
        self.goto(-210,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="center",font=FONT)


    def increase_level(self):
        self.level+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.color("cyan")
        self.write("GAME OVER ", align="center",font = ("comic sans",40,"normal"))
        exit()