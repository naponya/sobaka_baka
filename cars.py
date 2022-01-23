from turtle import Turtle
from random import randint
STEP = 5


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(self.random_color())
        self.shapesize(1, 2)
        self.goto(-260, self.random_y())

    def move(self):
        """Moves player by a given number of steps"""

        self.forward(STEP)

    def random_color(self):
        """Returns a random RGB color"""

        r = randint(90, 200)
        g = randint(90, 200)
        b = randint(90, 200)
        return r, g, b

    def random_y(self):
        """Returns a random y coordinate"""

        y = randint(-200, 200)
        return y
