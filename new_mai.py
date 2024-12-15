import turtle

def draw_shape(self):
    canvas = Screen()
    turtle.TurtleScreen._RUNNING=True
    t = turtle.Turtle()
    t.circle(self.r)
    canvas.exitonclick()
