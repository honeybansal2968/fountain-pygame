import pygame as pg
from settings import *
from random import uniform
import math
import cmath

pg.init()
size = (1000, 1000)
RED = (255, 0, 0)
screen = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()


def blitRotate(surf, image, pos, originPos, angle):
    # calcaulate the axis aligned bounding box of the rotated image
    w, h = image.get_size()
    box = [pg.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot
    pivot = pg.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(-angle)
    # pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0], pos[1] - originPos[1] - max_box[1])
    print("origin, ", origin)
    # origin = pg.math.Vector2(int(mouse[0]), int(mouse[1]))
    # get a rotated image
    rotated_image = pg.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)

    keys = pg.key.get_pressed()
    if keys[pg.K_f]:
        Bullet(pg.transform.rotate(bullet_image, -angle), bullet_pos, dir)
    # draw rectangle around the image
    # pg.draw.rect(surf, (255, 0, 0), (*origin, *rotated_image.get_size()), 2)


vec = pg.math.Vector2
pg.init()
""" Add player name top of the game who is playing now"""

dt = clock.tick(FPS) / 1000
hand_img = pg.image.load('laserRed.png')

hand_image = pg.transform.scale(pg.image.load('laserRed.png'), (60, 5))
w, h = hand_image.get_size()
player_img = pg.image.load('one_player4.png')


# angle = 0


class Player1(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (int(WIDTH / 2), int(HEIGHT / 2))
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.last_shot = pg.time.get_ticks()
        self.shoot_delay = 250
        self.jumping = True
        print("player1:", self.pos)

    def update(self):
        self.acc = vec(0, GRAVITY)
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LEFT]:
            self.acc.x = -0.5
        if keystate[pg.K_RIGHT]:
            self.acc.x = 0.5

        self.acc.x += self.vel.x * FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.midbottom = self.pos


class Bullet(pg.sprite.Sprite):
    def __init__(self, img, pos, dir):
        # self._layer = BULLET_LAYER
        self.groups = all_sprites, bullets
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = img
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        # self.image.set_colorkey(BLACK)
        # spread = uniform(-GUN_SPREAD, GUN_SPREAD)

        # velocity of bullet  = Bullet speed * direction vector
        self.vel = dir * 200 * uniform(0.9, 1.1)

        # spawn time of bullet after it get deleted
        self.spawn_time = pg.time.get_ticks()

    def update(self):
        self.pos += self.vel * dt
        self.rect.center = self.pos

        # bullet collision with walls
        if pg.sprite.spritecollideany(self, grounds):
            self.kill()

        # bullet deletion
        if pg.time.get_ticks() - self.spawn_time > 5000:
            self.kill()


class Ground(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.groups = all_sprites, grounds
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = self.x, self.y


def jump():
    hits = pg.sprite.spritecollide(player1, grounds, False)
    if hits:
        player1.vel.y = -20


all_sprites = pg.sprite.Group()
grounds = pg.sprite.Group()
for ground in GROUND_LIST:
    Ground(*ground)
bullets = pg.sprite.Group()
player1 = Player1(300, 400)

all_sprites.add(player1)

image = pg.image.load('laserRed.png')
w, h = image.get_size()
bullet_image = pg.Surface((2, 10))
bullet_image.fill(YELLOW1)
# angle = 0
done = False
while not done:
    clock.tick(FPS)
    screen.fill(BLACK)

    # keep loop running at the right speed

    # global direction
    # -------------------------------------process inputs-----------------------------------------------------------#
    mouse = pg.mouse.get_pos()

    pos = pg.math.Vector2(int(player1.pos[0] + 7), int(player1.pos[1] - 22))
    print("pos", pos)
    mouse_vec = pg.math.Vector2(mouse[0], mouse[1])
    mouse_mag = math.sqrt((mouse[0]) ** 2 + (mouse[1]) ** 2)
    rel_x = mouse[0] - pos[0]
    rel_y = mouse[1] - pos[1]
    angle = math.atan2(rel_x, rel_y) * 180 // 3.14
    # print("angle", angle)
    # bullet direction
    bullet_pos = pos[0] - 30, pos[1] - 20
    dir = vec(0, 1).rotate(-angle)

    print("mouse:", mouse)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            pg.quit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
                pg.quit()
            if event.key == pg.K_SPACE:
                jump()

            # if event.key == pg.K_f:
            #    Bullet(pg.transform.rotate(bullet_image, -angle), bullet_pos, dir)
    all_sprites.update()

    if player1.vel.y > 0:
        hits = pg.sprite.spritecollide(player1, grounds, False)
        if hits:
            for hit in hits:
                player1.pos.y = hit.rect.top
                player1.vel.y = 0

    all_sprites.draw(screen)
    blitRotate(screen, image, pos, (w // 2, h // 2), angle)

    # print("angle", angle * 180 // 3.14)

    pg.display.flip()

pg.quit()
