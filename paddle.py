from turtle import Turtle
STEP = 45
PADDLE_STARTING_COORDINATES = [(-320, 0), (310, 0)]
COLORS = ["red", "yellow", "green", "blue", "purple", "orange", 'white']


class Paddle(Turtle):

    def __init__(self, color_index):
        super().__init__()
        self.paddle_obj = self.create_paddle(color_index)

    def create_paddle(self, color_index):
        """Creates a paddle object from Turtle class
        with corresponding parameters"""

        paddle = Turtle('square')
        paddle.shapesize(7, 1)
        paddle.color(COLORS[color_index])
        paddle.penup()
        pos = PADDLE_STARTING_COORDINATES.pop()
        paddle.goto(pos)
        return paddle

    def up(self):
        """Shifts paddle up by a given number of steps"""

        if self.paddle_obj.ycor() >= 220:
            return
        else:
            y = self.paddle_obj.ycor()
            self.paddle_obj.sety(y + STEP)

    def down(self):
        """Shifts paddle down by a given number of steps"""

        if self.paddle_obj.ycor() <= -220:
            return
        else:
            y = self.paddle_obj.ycor()
            self.paddle_obj.sety(y - STEP)

