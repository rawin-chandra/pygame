import pygame
import os
import random

pygame.init()
screen = pygame.display.set_mode((800,600))

mario_sprite_sheet = pygame.image.load('mario.gif')
mario_back = pygame.image.load('mario_back_new.png')
effect = pygame.mixer.Sound('mario_sound.wav')
coin_effect = pygame.mixer.Sound('smb3_coin.wav')
mario_die_effect = pygame.mixer.Sound('mario_die.wav')
mario_jump_effect = pygame.mixer.Sound('smb3_jump.wav')
turtle_is_step_effect = pygame.mixer.Sound('smb3_stomp.wav')    #smb3_kick.wav  smb3_power-up.wav   smb3_mushroom_appears.wav
mushroom_appear_effect = pygame.mixer.Sound('smb3_power-up.wav')
power_up_effect = pygame.mixer.Sound('smb3_mushroom_appears.wav')

pygame.mixer.music.load('stage1.mp3')
pygame.mixer.music.play(-1)


font = pygame.font.SysFont("comicsansms", 72)

  #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด
mario_rect_right_big = pygame.Rect(10 ,25, 14, 29)
mario_rect_left_big = pygame.Rect(48 ,25, 14, 29)



mario_rect_walk1_right_big = pygame.Rect(115, 27, 17, 29)
mario_rect_walk2_right_big = pygame.Rect(140, 27, 17, 29)
mario_rect_walk1_left_big = pygame.Rect(140, 207, 17, 29)
mario_rect_walk2_left_big = pygame.Rect(166, 207, 17, 29)

turtle_rect_walk1_left = pygame.Rect(0,0,20,27)
turtle_rect_walk2_left = pygame.Rect(50,0,20,27)
turtle_rect_walk1_right = pygame.Rect(100,0,20,27)
turtle_rect_walk2_right = pygame.Rect(150,0,20,27)

turtle_die_rect = pygame.Rect(77,30,20,20)



mario_rect_right_jump_big = pygame.Rect(69,26,18,29)
mario_rect_left_jump_big = pygame.Rect(92,176,18,29)



mushroom_block_rect = pygame.Rect(440, 361, 60, 60);  #440, 361, 46, 46);   443, 256, 18, 18
mushroom_rect = pygame.Rect( 443, 256, 18, 18);

coin_rect = [ pygame.Rect(156,186,16,18),pygame.Rect(172,186,13,18),pygame.Rect(186,186,11,18),pygame.Rect(198,186,12,18),pygame.Rect(212,186,18,18) ]
coin_pos = [ [150,530],[178,530],[260,530],[333,530],[52,530] ]
coin_index = [ 2,3,0,1,2]

mario_walking = False
mario_face_turn = 1  # 0 = left, 1 = right
turtle_face_turn = 0
done = False
clock = pygame.time.Clock()   #ตัวกำหนด frame rate
mario_walk_count = 0
turtle_walk_count = 0
turtle_sprite_count = 0

loop_count = 0
coin_count = 0

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
points = 0

mario_alive = True
is_play_die_sound = False
is_play_jump_sound = False

mario_vel_x = 0
jump_step = 0
mario_is_jump = False
is_jump_finished = True
mario_is_fall = False
mario_is_big = False

turtle_alive = True

have_mushroom = False
mushroom_x = 443
mushroom_y = 360

screen_x = 0
diff_screen = 0

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


    def set_face_turn(self,turn):
        self.mario_face_turn= turn

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



background = Background(0,0,mario_back)

#mario_img = pygame.image.load(os.path.join('mario_small.gif')).convert()

mario = Mario(200,535,mario_sprite_sheet)


back_group = pygame.sprite.Group()
back_group.add(background)

player_group = pygame.sprite.Group()

turtle_img = pygame.image.load(os.path.join('turtle_small.gif')).convert()
turtle = [Turtle(500,525,turtle_img,10),Turtle(700,525,turtle_img,5),Turtle(1200,525,turtle_img,7),Turtle(1500,525,turtle_img,12)]

player_group.add(turtle)

mario_group = pygame.sprite.Group()
mario_group.add(mario)

def move_all_turtle(vel):
    for t in turtle:
        t.move(vel)

def check_collide():
    enemy = pygame.sprite.spritecollide(mario,player_group,False)
    if len(enemy) != 0:
        mario.dead()
    #if enemy != None:
    #    print(enemy)


while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    for event in pygame.event.get(): #เช็คอินพุท
        vel = 0

        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True

        if mario_alive == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mario.move(-10)
                    mario.set_face_turn(0)
                    mario.walk()
                    vel += 10
                elif event.key == pygame.K_RIGHT:
                    mario.move(10)
                    mario.set_face_turn(1)
                    mario.walk()
                    vel -= 10
                elif event.key == pygame.K_SPACE:
                    mario.jump()

            if mario.get_x() > background.get_x() + 400:
                background.move_screen(vel)
                mario.move(vel)
                move_all_turtle(vel)


    back_group.update()
    mario_group.update()
    player_group.update()

    check_collide()

    back_group.draw(screen)
    mario_group.draw(screen)
    player_group.draw(screen)

    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM)
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps
