from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.goto(position)
        if self.ycor() > -280:
            self.goto(self.xcor(),-280)

    def move_right(self):
        self.setheading(0)
        self.forward(35)

    def move_left(self):
        self.setheading(180)
        self.forward(35)


    def dragger(self):
        self.ondrag(None)
        position = self.pos()
        if self.ycor() > -280:
            self.goto(self.xcor(),-280)
        self.ondrag(self.dragger)








