from turtle import Turtle
import random
# screen dimension are 800x600
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
COLOR_INDEX = 0
BRICKS = []

class Brick(Turtle):


    def __init__(self,**kwargs):
        global COLOR_INDEX
        super().__init__()
        x = kwargs['x']
        y = kwargs['y']
        self.shape("square")
        self.color(COLORS[COLOR_INDEX])
        COLOR_INDEX += 1
        if COLOR_INDEX > len(COLORS) - 1:
            COLOR_INDEX = 0
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x, y)
        x += 4
        BRICKS.append(self)

    def delete(self):
        self.clear()

    def reset(self):
        self.reset()
        for brik in self:
            brik.delete()
