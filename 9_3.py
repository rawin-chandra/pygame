import pygame
import os
import random

pygame.init()
screen = pygame.display.set_mode((800,600))

mario_sprite_sheet = pygame.image.load('mario.gif')
mario_back = pygame.image.load('mario_back_new.png')

done = False
clock = pygame.time.Clock()   #ตัวกำหนด frame rate

class Background(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        super().__init__()
        self.image = img
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.y = y

    def update(self):
        pass

class Mario(pygame.sprite.Sprite):

    def __init__(self,x,y,img):
        mario_rect_right = pygame.Rect(11,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด
        mario_rect_left = pygame.Rect(30,4,14,17)

        super().__init__()
        self.img = img
        self.img.set_colorkey((255,255,255))

        self.image = img.subsurface(mario_rect_right)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.y = y

        self.mario_face_turn = 1
        self.jump_count = 0
        self.is_jump = False
        self.is_walk = False
        self.walk_step = 0

    def update(self):
        pass

class Turtle(pygame.sprite.Sprite):
    def __init__(self,x,y,img,loop_count):
        super().__init__()

        self.image = img
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.y = y

    def update(self):
        pass


background = Background(0,0,mario_back)

back_group = pygame.sprite.Group()
back_group.add(background)
mario = Mario(200,535,mario_sprite_sheet)
mario_group = pygame.sprite.Group()
mario_group.add(mario)

turtle_img = pygame.image.load(os.path.join('turtle_small.gif')).convert()
turtle = [Turtle(500,525,turtle_img,10),Turtle(700,525,turtle_img,5),Turtle(1200,525,turtle_img,7),Turtle(1500,525,turtle_img,12)]

player_group = pygame.sprite.Group()
player_group.add(turtle)

while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True

    back_group.update()
    mario_group.update()
    player_group.update()
    back_group.draw(screen)
    mario_group.draw(screen)
    player_group.draw(screen)


    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM)
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps
