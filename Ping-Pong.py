

from cgitb import reset
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
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        pass
    def update_r(self):
        pass

racket1 = Player('object3.jpg', 5, 200, 30, 60, 10)
racket2 = Player('object4.jpg', 650, 300, 30, 60, 10)
ball = GameSprite('object5.png', 100, 300, 50, 50, 10)



finish = False
run = True
while run:
    window.blit(background, (0, 0))
    racket1.reset()
    racket2.reset()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(FPS)
