import pygame
from settings import *
from player import Player
from ball import *
from ray_casting import ray_casting
from drawing import Drawing
from state_of_game import *
from rules import check_rules
import time

pygame.init()
pygame.display.set_caption("Robot and balls")
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
balls = [Ball() for i in range(0, count_of_ball)]
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(sc, sc_map)
state_of_game = Running()

while state_of_game.name == 'running':
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            state_of_game.switch(Pause)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        player.movement()
        [ball.movement() for ball in balls]
        walls = ray_casting(player, drawing.textures)

        sc.fill(BLACK)
        drawing.background(player.angle)
        drawing.world(walls + [ball.locate(player, walls) for ball in balls])
        drawing.fps(clock)
        drawing.time_of_game()
        drawing.mini_map(player, balls)
        pygame.display.flip()
        clock.tick()
        check_rules(balls, player, state_of_game)
sc.fill(BLACK)
drawing.print_text('Game over', (HALF_WIDTH-100, HALF_HEIGHT-100), WHITE)
drawing.print_text('Your time: {}'.format(drawing.time_of_game()), (HALF_WIDTH+150, HALF_HEIGHT+150), WHITE)
pygame.display.flip()
time.sleep(1)