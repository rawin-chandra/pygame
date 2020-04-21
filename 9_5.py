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


    def move_screen(self,vel):
        self.rect.left += vel

    def update(self):
        pass

    def get_x(self):
        return self.rect.x

class Mario(pygame.sprite.Sprite):

    def __init__(self,x,y,img):
        mario_rect_right = pygame.Rect(11,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด
        mario_rect_left = pygame.Rect(30,4,14,17)

        super().__init__()
        self.img = img
        self.img.set_colorkey((255,255,255))

        #r1 = pygame.Rect(0,0,14,17)
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
        mario_rect_right = pygame.Rect(11,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด
        mario_rect_left = pygame.Rect(30,4,14,17)
        mario_rect_walk_left = [pygame.Rect(138,4,20,20) , pygame.Rect(211,4,20,20)]
        mario_rect_walk_right = [ pygame.Rect(114,4,20,20),pygame.Rect(186,4,20,20) ]

        if self.is_jump == True:
            self.jump_update()

            self.jump_count += 1
            if self.jump_count >= 20:
                self.jump_count = 0
                self.is_jump = False

        elif self.is_walk == True:
            if self.mario_face_turn == 0:
                self.image = self.img.subsurface(mario_rect_walk_left[self.walk_step])
                self.walk_step += 1
                self.walk_step %= 2
            elif self.mario_face_turn == 1:
                self.image = self.img.subsurface(mario_rect_walk_right[self.walk_step])
                self.walk_step += 1
                self.walk_step %= 2
            self.is_walk = False
        else:
            if self.mario_face_turn == 0:
                self.image = self.img.subsurface(mario_rect_left)
            elif self.mario_face_turn == 1:
                self.image = self.img.subsurface(mario_rect_right)

    def move(self,vel):
        self.rect.x += vel
        if vel < 0:
            self.mario_face_turn = 0
        else:
            self.mario_face_turn = 1

    def get_x(self):
        return self.rect.x

    def dead(self):
        mario_die_rect = pygame.Rect(339,263,18,20)
        self.image = self.img.subsurface(mario_die_rect)

    def jump(self):
        self.is_jump = True

    def walk(self):
        self.is_walk = True

    def jump_update(self):
        mario_rect_right_jump = pygame.Rect(48,3,20,20)
        mario_rect_left_jump = pygame.Rect(71,3,20,20)

        if self.mario_face_turn == 1:
            self.image = self.img.subsurface(mario_rect_right_jump)
            self.rect.x += 1
            if self.jump_count < 10:
                self.rect.y -= 12
            else:
                self.rect.y += 12

        elif self.mario_face_turn == 0:
            self.image = self.img.subsurface(mario_rect_left_jump)
            self.rect.x -= 1
            if self.jump_count < 10:
                self.rect.y -= 12
            else:
                self.rect.y += 12


class Turtle(pygame.sprite.Sprite):
    def __init__(self,x,y,img,loop_count):
        super().__init__()

        self.image = img
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.y = y
        self.loop_count = loop_count


    def update(self):
        self.loop_count += 1
        if self.loop_count < 20:
            self.rect.x += 1
        else:
            self.rect.x -= 1

        if self.loop_count >= 40:
            self.loop_count = 0


    def move(self,vel):
        self.rect.x += vel


def move_all_turtle(vel):
    for t in turtle:
        t.move(vel)

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

mario_alive = True

while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    vel = 0
    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True
        if mario_alive == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mario.move(-10)
                    mario.walk()
                    vel += 10
                elif event.key == pygame.K_RIGHT:
                    mario.move(10)
                    mario.walk()
                    vel -= 10

        if mario.get_x() > background.get_x() + 400:
            background.move_screen(vel)
            mario.move(vel)
            move_all_turtle(vel)


    back_group.update()
    mario_group.update()
    player_group.update()
    back_group.draw(screen)
    mario_group.draw(screen)
    player_group.draw(screen)


    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM)
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps
