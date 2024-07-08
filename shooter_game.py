from typing import Any
from pygame import *
from random import *
print("This is the new version")
print('asd')
window = display.set_mode((700, 500))
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
print("Pull need")
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # each sprite must store an image property
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
        # each sprite must store the rect property it is inscribed in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
bullets = sprite.Group()

class Rocket(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700-55:
            self.rect.x += self.speed
    
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.x, 445, 7)
        bullets.add(bullet)
print("Hello")
class UFO(GameSprite):
    def update(self):
        global missed
        self.rect.y += self.speed
        if self.rect.y > 445:
            self.rect.y = 0
            self.rect.x = randint(0, 645)
            self.speed = randint(1, 6)
            missed += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed

font.init()
font1 = font.SysFont('Arial', 40)
lost = font1.render("YOU LOSE!!!", True, (255, 0, 0))
print('hello')
score = 0 

missed = 0
font2 = font.SysFont('Arial', 40)
clock = time.Clock()
FPS = 60
game = True
rocket = Rocket('rocket.png', 100, 445, 10)
finish = False

ufos = sprite.Group()
for i in range(10):
    ufo = UFO('ufo.png', randint(0, 645), 0, randint(1, 5))
    ufos.add(ufo)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.fire()
        


    collides = sprite.groupcollide(bullets, ufos, True, True)
    for i in collides:
        score += 1
        ufo = UFO('ufo.png', randint(0, 645), 0, randint(1, 5))
        ufos.add(ufo)

    if sprite.spritecollide(rocket, ufos, False) and missed > 5:
        finish = True
        window.blit(lost, (200, 200 ))

    if finish == False:
        window.blit(background, (0, 0))
        ufos.draw(window)
        bullets.draw(window)
        rocket.reset()


        rocket.update()
        bullets.update()
        ufos.update()

    scr = font2.render("Score:" + str(score), True, (255, 255, 255))
    window.blit(scr, (0,0))

    miss = font2.render("Missed:" + str(missed), True, (255, 255, 255))
    window.blit(miss, (0,30))


    clock.tick(FPS)
    display.update()
