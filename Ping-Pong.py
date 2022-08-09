from pygame import *
from random import randint
from time import time as timer

window = display.set_mode((1200, 720))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('galaxy.jpg'), (1200, 720))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

game = True
clock = time.Clock()
FPS = 60
finish = False
rel_time = False
num_fire = 0
life = 10
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, width, height, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        pass
    def update_r(self):
        pass


finish = False
run = True
while run:
    window.blit(background, (0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(FPS)
