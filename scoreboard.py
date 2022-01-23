from turtle import Turtle
FONT = ('Cooper Black', 15, 'bold')
FONT2 = ('Cooper Black', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color((20, 2, 6))
        self.goto(-230, 265)
        self.score = 0

    def score_up(self):
        """Increases self.score by 1"""

        self.score += 1

    def update_score(self):
        """Writes current score in the left top
         corner of the window"""

        self.clear()
        self.write(arg=f"Roads Crossed: {self.score}/5", font=FONT)

    def win(self):
        """Whites congratulations to player
        in the center of the screen"""

        self.goto(0, 0)
        self.write(arg="Congratulations\non your success!", align='center', font=FONT2)

    def lose(self):
        """Whites game over in the center of the screen"""

        self.goto(0, 0)
        self.write(arg="Game Over", align='center', font=FONT2)
