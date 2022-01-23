from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from paddle import COLORS

screen = Screen()
screen.title('A Little Bit Unpredictable Pong Game! Have fun!')
screen.setup(700, 600)
screen.bgcolor('black')
screen.colormode(255)
screen.tracer(0)

# -------------USERS' INPUT-------------
pl1 = int(screen.numinput("Welcome to A Little Bit Unpredictable Pong Game!",
                      "Your goal is to reach 10 points as first.\nLeft player, choose your color:\n1.red 2.yellow 3.green 4.blue 5.purple 6.orange 7.white"))
while pl1 not in range(1, 8):
    pl1 = int(screen.numinput("Ouch!",
                          "Left player, there's no that color! Choose again:\n1.red 2.yellow 3.green 4.blue 5.purple 6.orange 7.white"))

pl2 = int(screen.numinput("Welcome you, the second one!",
                      "Your goal is to reach 10 points as first.\nRight player, choose your color:\n1.red 2.yellow 3.green 4.blue 5.purple 6.orange 7.white"))
while pl2 == pl1 or pl2 not in range(1, 8):
    while pl2 == pl1:
        pl2 = int(screen.numinput("Ouch!",
                              f"There could be only one {COLORS[pl1-1]} paddle! Try to be first next time:\n1.red 2.yellow 3.green 4.blue 5.purple 6.orange 7.white"))
    while pl2 not in range(1, 8):
        pl2 = int(screen.numinput("Ouch!",
                              "Right player, there's no that color! Choose again:\n1.red 2.yellow 3.green 4.blue 5.purple 6.orange 7.white"))


# -------------CREATING INSTANCES AND BID THEM ON KEYS-------------
paddle_right = Paddle(pl2 - 1)
paddle_left = Paddle(pl1 - 1)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddle_right.up, 'Up')
screen.onkey(paddle_right.down, 'Down')
screen.onkey(paddle_left.up, 'w')
screen.onkey(paddle_left.down, 's')

play = True
sleep_time = 0.08

# -------------THE GAME ITSELF-------------
while play:
    scoreboard.print_score()
    screen.update()
    time.sleep(sleep_time)
    ball.move()

    x_right = paddle_right.paddle_obj.xcor()
    y_right = paddle_right.paddle_obj.ycor()

    y_left = paddle_left.paddle_obj.ycor()
    x_left = paddle_left.paddle_obj.xcor()

    # -------------IF LEFT WINS-------------
    if ball.ball.xcor() > 360:
        scoreboard.score_up_left()
        if scoreboard.left_score == 10:
            scoreboard.win(pl1 - 1, 'l')
            break
        sleep_time = ball.reset()

    # -------------IF RIGHT WINS-------------
    if ball.ball.xcor() < -370:
        scoreboard.score_up_right()
        if scoreboard.right_score == 10:
            scoreboard.win(pl2 - 1, '(')
            break
        sleep_time = ball.reset()

    # -------------PADDLE COLLUSION-------------
    if ball.ball.distance(x_right, y_right) < 60 or ball.ball.distance(x_left, y_left) < 60:
        if ball.ball.xcor() < -300 or ball.ball.xcor() > 290:
            ball.collusion_paddle()
            ball.ball.forward(15)
            if sleep_time > 0.01:
                sleep_time -= 0.01

    # -------------WALL COLLUSION-------------
    if ball.ball.ycor() >= 300 or ball.ball.ycor() <= -290:
        ball.collusion_wall()
        ball.ball.forward(15)

screen.exitonclick()
