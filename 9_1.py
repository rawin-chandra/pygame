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



background = Background(0,0,mario_back)

back_group = pygame.sprite.Group()
back_group.add(background)


while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True

    back_group.update()
    back_group.draw(screen)


    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM)
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps
