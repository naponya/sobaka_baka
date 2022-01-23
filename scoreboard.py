from turtle import Turtle
from paddle import COLORS
ALIGN = 'center'
FONT = ('Bauhaus 93', 32, 'bold')
FONT2 = ('Bauhaus 93', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.right_score = 0
        self.left_score = 0
        self.up()
        self.goto(-0, 235)
        self.color("white")

    def score_up_left(self):
        """Rises score of the left player by 1"""

        self.left_score += 1

    def score_up_right(self):
        """Rises score of the right player by 1"""

        self.right_score += 1

    def print_score(self):
        """Clears the screen and prints current score
        on the top side of the playground"""

        self.clear()
        to_print = f"{self.left_score} : {self.right_score}"
        self.write(arg=to_print, align=ALIGN, font=FONT)

    def win(self, color_index, who='l'):
        """Called when either of players wins.
        Prints final score and congratulates winner
        with text in the center of playground"""

        self.print_score()
        self.goto(0, -20)
        if who != 'l':
            to_print = "Right player wins\nThat was a good game!"
            self.write(arg=to_print, align=ALIGN, font=FONT2)
            print(':(')
        else:
            to_print = f"Left player wins!\nCongratulations to my lovely player! \nI'm happy to see your victory!\nBy the way, {COLORS[color_index]} is my favorite color too!"
            self.write(arg=to_print, align=ALIGN, font=FONT2)
