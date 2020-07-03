from state_of_game import *
import math


def distance(a, b):
    distance = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
    return distance


def intersections_of_circles(a, b):
    intersection = True if a.r - b.r < distance(a, b) < a.r + b.r else False
    return intersection


def check_rules(balls, player, state_of_game):
    for ball in balls:
        if intersections_of_circles(ball, player):
            state_of_game.switch(Close)
