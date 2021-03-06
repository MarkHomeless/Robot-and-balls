import pygame
from settings import *
from map import mini_map

class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font_fps = pygame.font.SysFont('Arial', 28, bold=True)
        self.font_text = pygame.font.SysFont('Arial', 52, bold=True)
        self.font_time = pygame.font.SysFont('Arial', 32, bold=True)
        self.textures = {'1': pygame.image.load('img/wall1.png').convert(),
                         '2': pygame.image.load('img/wall2.png').convert(),
                         'S': pygame.image.load('img/sky3.png').convert()
                         }

    def background(self, angle):
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font_fps.render(display_fps, 0, DARKORANGE)
        self.sc.blit(render, FPS_POS)

    def mini_map(self, player, balls):
        self.sc_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        map_ball_list = [(int(ball.x // MAP_SCALE), int(ball.y // MAP_SCALE)) for ball in balls]
        pygame.draw.line(self.sc_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, GREEN, (int(map_x), int(map_y)), player_map_radius)
        for map_ball in map_ball_list:
            pygame.draw.circle(self.sc_map, RED, map_ball, ball_map_radius)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, DARKBROWN, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)
    def print_text(self, text, text_pos, color):
        render = self.font_text.render(text, 0, color)
        self.sc.blit(render, text_pos)
    def time_of_game(self):
        time = str(pygame.time.get_ticks() // 1000)
        render = self.font_time.render('time:' + time, 0, BLACK)
        self.sc.blit(render, TIME_POS)
        return time