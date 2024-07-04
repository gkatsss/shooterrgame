#Create your own shooter
from typing import Any
from pygame import *
from random import *
from class_file import *

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Hero(GameSprite):
    def movement(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= 10
        if keys_pressed[K_DOWN]:
            self.rect.y += 10
        if keys_pressed[K_LEFT]:
            self.rect.x -= 10
        if keys_pressed[K_RIGHT]:
            self.rect.x += 10
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.x+ 35, 450, 10, 50, 50)
        bullets.add(bullet) 
missed = 0

class Enemy(GameSprite):        
    def movement(self):
        global missed
        self.rect.x += self.speed
        if self.rect.x > 500:
            missed += 1
            self.rect.y = 0

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed



window = display.set_mode((700, 500))

backround = transform.scale(image.load('galaxy.jpg'), (700,500))
hero = Hero('rocket.png', 10, 200, 10)



font.init()
score = 0


rocket = ('rocket.png', 100, 400, 10)



ufos = sprite.Group()
for i in range(10):
    ufo = Enemy('ufo.png',randint(0, 600), 0, randint(0, 5)) 
    ufos.add(ufo)

    


font1 = font.Font(None, 30)
finish =  False
clock = time.Clock()
bullets = sprite.Group()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    rocket.fire()
    
    win = font1.render('YOU WIN:' , True, (255, 255, 255))
    if sprite.spritecollide(rocket, ufos, False):
        window.blit(win, (300, 200))
        finish = True
    font1 = font.Font(None, 30)
    score_text = font1.render('SCORE:' + str(score), True, (255, 255, 255))




    if not finish:
        window.blit(backround, (0, 0))
        rocket.reset()
        rocket.update()

        ufos.draw(window)
        ufos.update()

        collides = sprite.groupcollide(ufos, bullets, True, True)
        for col in collides:
            ufo = Enemy('ufo.png',randint(0, 600), 0, randint(0, 5), 80, 80)
            ufos.add(ufo)

        


        font1 = font.Font(None, 30)
        score_missed = font1.render('MISSED:' + str(missed), True, (255, 255, 255))

        window.blit (score_missed, (20, 10))


        bullets.draw(window)
        bullets.update()


        FPS = 60
        display.update()
        clock.tick(FPS)
        


































        



