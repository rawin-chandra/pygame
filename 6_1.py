import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
mario = pygame.image.load('mario.gif')
turtle = pygame.image.load('enemies.gif')
mario_back = pygame.image.load('mario_back.png')
effect = pygame.mixer.Sound('mario_sound.wav')
coin_effect = pygame.mixer.Sound('smb3_coin.wav')
pygame.mixer.music.load('stage1.mp3')
pygame.mixer.music.play(-1)
mario.set_colorkey((255,255,255))
turtle.set_colorkey((255,255,255))
mario_x = 100 #65
mario_y = 535
mario_w = 14
mario_h = 14

turtle_x = 500 #600 #65
turtle_y = 525

mario_rect_right = pygame.Rect(11,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด
mario_rect_left = pygame.Rect(30,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด
mario_rect_walk1_left = pygame.Rect(138,4,20,20)
mario_rect_walk2_left = pygame.Rect(211,4,20,20)
mario_rect_walk1_right = pygame.Rect(114,4,20,20)
mario_rect_walk2_right = pygame.Rect(186,4,20,20)

turtle_rect_walk1_left = pygame.Rect(0,0,20,27)
turtle_rect_walk2_left = pygame.Rect(50,0,20,27)
turtle_rect_walk1_right = pygame.Rect(100,0,20,27)
turtle_rect_walk2_right = pygame.Rect(150,0,20,27)

coin_rect = [ pygame.Rect(156,186,16,18),pygame.Rect(172,186,13,18),pygame.Rect(186,186,11,18),pygame.Rect(198,186,12,18),pygame.Rect(212,186,18,18) ]
coin_pos = [ (150,530),(178,530),(260,530),(333,530),(452,530) ]
coin_index = [ 2,3,0,1,2]

mario_walking = False
mario_face_turn = 1  # 0 = left, 1 = right
turtle_face_turn = 0
done = False
clock = pygame.time.Clock()   #ตัวกำหนด frame rate
mario_walk_count = 0
turtle_walk_count = 0

turtle_count = 0
loop_count = 0
coin_count = 0

def draw_mario_walk():
    global screen,mario_walk_count
    if mario_walk_count == 0:
        if mario_face_turn == 0:
            screen.blit(mario,(mario_x,mario_y),mario_rect_walk1_left)
        else:
            screen.blit(mario,(mario_x,mario_y),mario_rect_walk1_right)
    elif mario_walk_count == 1:
        if mario_face_turn == 0:
            screen.blit(mario,(mario_x,mario_y),mario_rect_walk2_left)
        else:
            screen.blit(mario,(mario_x,mario_y),mario_rect_walk2_right)
    mario_walk_count += 1
    if mario_walk_count == 2:
        mario_walk_count = 0

def draw_turtle_walk():
    global screen,turtle_walk_count
    if turtle_walk_count == 0:
        if turtle_face_turn == 0:
            screen.blit(turtle,(turtle_x,turtle_y),turtle_rect_walk1_left)
        else:
            screen.blit(turtle,(turtle_x,turtle_y),turtle_rect_walk1_right)
    elif turtle_walk_count == 1:
        if turtle_face_turn == 0:
            screen.blit(turtle,(turtle_x,turtle_y),turtle_rect_walk2_left)
        else:
            screen.blit(turtle,(turtle_x,turtle_y),turtle_rect_walk2_right)
    turtle_walk_count += 1
    if turtle_walk_count == 2:
        turtle_walk_count = 0

def turtle_walk():
    global turtle_count,turtle_x
    if abs(turtle_x - mario_x) > 100:
        if turtle_count < 10:
            turtle_x += 5
            turtle_face_turn = 1
        else:
            turtle_x -= 5
            turtle_face_turn = 0
        turtle_count += 1
        if turtle_count >= 20:
            turtle_count = 0
    else:
        #check direction of mario
        #if mario is left of turtle
        if mario_x < turtle_x:
            turtle_x -= 5
            turtle_face_turn = 0
        else:
            turtle_x += 5
            turtle_face_turn = 1
        turtle_count = 0

def draw_coin():
    global screen,coin_count

    for i in range(len(coin_pos)):
        if coin_pos[i] == -1:
            continue

        screen.blit(mario,coin_pos[i],coin_rect[  coin_index[i]  ])

        if coin_count % 5 == 0:
            coin_index[i] += 1
            coin_index[i] %= 5

def check_collide():
    mario = pygame.Rect(mario_x,mario_y,mario_w,mario_h)
    #print(mario)
    for i in range(len(coin_pos)):
        if coin_pos[i] == -1:
            continue
        coin = pygame.Rect( coin_pos[i][0], coin_pos[i][1], 18,18)

        if mario.colliderect(coin):
            coin_effect.play()
            coin_pos[i] = -1


while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mario_x -= 10
                effect.play()
                mario_walking = True
                mario_face_turn = 0
            elif event.key == pygame.K_RIGHT:
                mario_x += 10
                effect.play()
                mario_walking = True
                mario_face_turn = 1
        else:
            mario_walking = False

    check_collide()

    screen.blit(mario_back,(0,0))

    if mario_walking == True:
        draw_mario_walk()
    else:
        if mario_face_turn == 0:
            screen.blit(mario,(mario_x,mario_y),mario_rect_left)
        else:
            screen.blit(mario,(mario_x,mario_y),mario_rect_right)

    if loop_count % 10 == 0:
        turtle_walk()

    draw_turtle_walk()
    draw_coin()

    coin_count += 1
    loop_count += 1

    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM)
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps
