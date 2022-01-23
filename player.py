from turtle import Turtle
from cars import STEP
STEP_PLAYER = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color((59, 20, 24))
        self.penup()
        self.seth(90)
        self.goto(0, -280)

    def move(self):
        """Moves player by a given number of steps"""

        print("GO!")
        self.forward(STEP_PLAYER)

    def quit(self):
        """Makes layer move to the right of
        the screen by a given number of steps"""

        print("💀")
        self.goto(self.xcor() + STEP, self.ycor())
