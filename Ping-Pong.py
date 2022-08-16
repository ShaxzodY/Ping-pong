from cgitb import reset
from pygame import *
from random import randint
from time import time as timer

win_height = 450
win_width = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')
background = transform.scale(image.load('background1.jpg'), (win_width, win_height))

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
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width -80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
        

speed_x = 3
speed_y = 3
racket1 = Player('Pong1.png', 5, 200, 30, 60, 10)
racket2 = Player('Pong1.png', win_width-50, 300, 30, 60, 10)
ball = GameSprite('tenis_ball.png', 100, 300, 50, 50, 10)


font.init()
finish = False
run = True
win1 = font.SysFont('Roboto', 40).render('Winner: Player 1!', True, (255, 255, 255))
win2 = font.SysFont('Roboto', 40).render('Winner: Player 2!', True, (255, 255, 255))

while run:
    window.blit(background, (0, 0))
    racket1.reset()
    racket2.reset()
    ball.reset()
    racket1.update_l()
    racket2.update_r()
    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if sprite.collide_rect(ball, racket2) or sprite.collide_rect(ball, racket1):
        speed_x *= -1

    if ball.rect.y > win_height-30 or ball.rect.y < 0:
        speed_y *= -1

    if ball.rect.x < 0:
        finish = True
        window.blit(win2, (win_width/2 - 50, win_width/2))
    if ball.rect.x > win_width:
        finish = True
        window.blit(win1, (win_width/2 - 50, win_width/2))

    for e in event.get():
        if e.type == QUIT:
            run = False

    display.update()
    clock.tick(FPS)
