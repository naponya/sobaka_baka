from turtle import Turtle
from random import choice, randint
STARTING_HEADINGS = [15, 165, 30, 150, 345, 330, 165, 150]
STEP = 12


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball = self.create_ball()
        self.ball.setheading(choice(STARTING_HEADINGS))

    def create_ball(self):
        """Creates a ball object from Turtle class
         with corresponding parameters"""

        ball = Turtle('circle')
        ball.color('white')
        ball.penup()
        return ball

    def move(self):
        """Moves ball by a given number of steps"""

        self.ball.forward(STEP)

    def random_color(self):
        """Randomly changes ball's color using RGB pallet"""

        r = randint(70, 255)
        g = randint(70, 255)
        b = randint(70, 255)
        self.ball.color(r, g, b)

    def collusion_wall(self):
        """Should be called when a ball hits a wall.
        Changes heading of the ball"""

        if self.ball.heading() in range(0, 91) or self.ball.heading() in range(181, 270):
            self.ball.right(130)
        elif self.ball.heading() in range(91, 181) or self.ball.heading() in range(270, 360):
            self.ball.left(130)
        self.random_color()

    def collusion_paddle(self):
        """Should be called when a ball hits a paddle.
        Changes heading of a ball according to it's angle"""

        if self.ball.heading() in range(160, 181) or self.ball.heading() in range(340, 360):
            self.ball.right(155)
        elif self.ball.heading() in range(180, 201) or self.ball.heading() in range(0, 21):
            self.ball.left(155)
        elif self.ball.heading() in range(140, 181) or self.ball.heading() in range(310, 360):
            self.ball.right(140)
        elif self.ball.heading() in range(180, 222) or self.ball.heading() in range(0, 42):
            self.ball.left(140)
        elif self.ball.heading() in range(90, 181) or self.ball.heading() in range(270, 360):
            self.ball.right(115)
        elif self.ball.heading() in range(180, 270) or self.ball.heading() in range(0, 90):
            self.ball.left(115)
        self.random_color()

    def reset(self):
        """Resets the ball position to 0,0.
        Reverses heading of the ball by 180°"""

        self.ball.goto(0, 0)
        self.ball.seth(self.ball.heading() + 180)
        return 0.08
