import pygame as pg
vec = pg.math.Vector2

""" GAME SETTINGS"""
WIDTH = 800
HEIGHT = 600
FPS = 60
FRICTION = -0.12
GRAVITY = 0.8

""" Add player name top of the game who is playing now"""
"""different seasons of maps and random choice among them"""
"""gun unlock at level ups"""
"""for different season there are special equipments which will be unlocked as level ups"""
"""after winning , winner will see some kind of face of his enemy"""
"""after sometime a crown or winning object will appear to win the match in short time"""
"""acid map, in which ground become acid and when player touches it it'll die"""
"""make different map unlock when player plays online and keep them lock when offline until level ups"""
""" COLORS"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
GREEN1 = (45, 255, 0)
GREEN2 = (78, 255, 0)
GREEN3 = (126, 255, 0)
GREEN4 = (184, 255, 0)
YELLOW1 = (210, 255, 0)
YELLOW2 = (255, 255, 0)
YELLOW3 = (255, 200, 0)
YELLOW4 = (255, 159, 0)
ORANGE1 = (255, 123, 0)
ORANGE2 = (255, 89, 0)
RED1 = (255, 47, 0)
RED = (255, 0, 0)
LIGHTPINK = (255, 150, 190)
LIGHTGRAY = (203, 255, 255)

""" PLAYER SETTINGS """
SPEEDX = 5
SPEEDY = 2
PLAYER_JUMP = 5

"""HAND_SETTINGS"""
HAND_ROTATE_SPEED = 20
BARREL_OFFSET = vec(-20, -10)

""" GROUND SETTINGS """
GROUND_LIST = [(0, HEIGHT - 2, WIDTH * 2, 30),
                 (int(WIDTH / 2 - 50), int(HEIGHT * 3 / 4 - 50), 100, 30),
                 (125, HEIGHT - 350, 70, 20),
                 (350, 200, 100, 20),
                 (175, 100, 100, 20)]
