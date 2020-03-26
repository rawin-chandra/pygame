import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

mario = pygame.image.load('mario3.gif')
mario_back = pygame.image.load('mario_back.png')

mario_stuff = pygame.image.load('mario_stuff.png')

mario.set_colorkey((255,255,255))
mario_stuff.set_colorkey((0,0,0))

pygame.mixer.music.load('stage1.mp3')
pygame.mixer.music.play(-1)

mario_rect_left_walk = pygame.Rect(209,1,20,20)
mario_rect_right_walk = pygame.Rect(185,1,20,20)
mario_rect_left_stand = pygame.Rect(35,5,18,17)
mario_rect_right_stand = pygame.Rect(11,5,18,17)
mario_die = pygame.Rect(438,3,18,17)
mario_x = 30
mario_y = 535

t = pygame.Rect(71,330,19,21)
t_x = 500
t_y = 535
count = 0
done = False
turtle_walk_step = 0
turtle_dir = True
mario_face_turn = False    #right
mario_walk_step = True
mario_walk = False
mario_live = True

clock = pygame.time.Clock()
while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True
        if mario_live == False:
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mario_x -= 10
                mario_face_turn = True
                mario_walk = True
            if event.key == pygame.K_RIGHT:
                mario_x += 10
                mario_face_turn = False
                mario_walk = True
        else:
            mario_walk = False
    screen.blit(mario_back,(0,0))

    if mario_live == False:
        screen.blit(mario,(mario_x,mario_y),mario_die)
    else:
        if mario_face_turn == True:
            if mario_walk == True:
                if mario_walk_step == True:
                    screen.blit(mario,(mario_x,mario_y),mario_rect_left_walk)
                    mario_walk_step = False
                else:
                    mario_walk_step = True
                    screen.blit(mario,(mario_x,mario_y),mario_rect_left_stand)
            else:
                screen.blit(mario,(mario_x,mario_y),mario_rect_left_stand)

        else:
            if mario_walk == True:
                if mario_walk_step == True:
                    screen.blit(mario,(mario_x,mario_y),mario_rect_right_walk)
                    mario_walk_step = False
                else:
                    mario_walk_step = True
                    screen.blit(mario,(mario_x,mario_y),mario_rect_right_stand)
            else:
                screen.blit(mario,(mario_x,mario_y),mario_rect_right_stand)

        screen.blit(mario_stuff,(t_x,t_y),t)
    count += 1
    if count >= 30:
        if turtle_dir == True:
            t_x += 5
        else:
            t_x -= 5
        count = 0
        turtle_walk_step += 1
        if turtle_walk_step >= 5:
            if turtle_dir == True:
                turtle_dir = False
            else:
                turtle_dir = True
            turtle_walk_step = 0

    mario_r = pygame.Rect(mario_x,mario_y,20,20)
    turtle_r = pygame.Rect(t_x,t_y,19,21)
    if mario_r.colliderect(turtle_r):
        mario_live = False

    pygame.display.flip()
    clock.tick(30);
