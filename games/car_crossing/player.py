STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("light green")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.UP()
        self.DOWN()

    def UP(self):
        self.forward(MOVE_DISTANCE)

    def DOWN(self):
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)





    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False