"""The purpose of this game is to help the turtle
    cross 5 roads. And then you win"""

from turtle import Screen
from player import Player
from time import sleep
from cars import Car
from random import choice
from scoreboard import Scoreboard

true_false = [True, False, False, False, False]

screen = Screen()
screen.setup(500, 600)
screen.tracer(0)
screen.colormode(255)
screen.bgcolor((252, 227, 249))
screen.title("Help the Turtle Cross a Road!")

cars = []


def to_begin_with():
    for i in range(6):
        car = Car()
        cars.append(car)


player = Player()
scoreboard = Scoreboard()
score_fin = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

to_begin_with()
sleep_time = 0.1

while True:
    scoreboard.update_score()

    # -------------RANDOMLY CREATE A CAR-------------
    if choice(true_false):
        car = Car()
        cars.append(car)

    # -------------MOVE ALL CARS-------------
    for car in cars:
        car.move()

    # -------------SCREEN UPDATE-------------
    screen.update()
    sleep(sleep_time)

    # -------------CHECK IF CAR CRUSHED INTO PLAYER-------------
    for car in cars:
        if player.distance(car) < 18:
            screen.onkeypress(None, "Up")
            score_fin.lose()
            player.quit()

    # -------------CHECK IF PLAYER REACHED THE OTHER SIDE-------------
    if player.ycor() >= 280:
        sleep_time *= 0.7
        scoreboard.score_up()
        player.goto(0, -280)

    # -------------CHECK IF PLAYER WINS-------------
    if scoreboard.score == 5:
        score_fin.win()
        player.ht()
        screen.onkeypress(None, "Up")
