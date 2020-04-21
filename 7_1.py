import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
mario = pygame.image.load('mario.gif')
turtle = pygame.image.load('enemies.gif')
mario_back = pygame.image.load('mario_back.png')
effect = pygame.mixer.Sound('mario_sound.wav')
coin_effect = pygame.mixer.Sound('smb3_coin.wav')
mario_die_effect = pygame.mixer.Sound('mario_die.wav')
mario_jump_effect = pygame.mixer.Sound('smb3_jump.wav')

pygame.mixer.music.load('stage1.mp3')
pygame.mixer.music.play(-1)
mario.set_colorkey((255,255,255))
font = pygame.font.SysFont("comicsansms", 72)
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

mario_rect_right_jump = pygame.Rect(48,3,20,20)
mario_rect_left_jump = pygame.Rect(71,3,20,20)

mario_die_rect = pygame.Rect(339,263,18,20)

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
    global screen,turtle_sprite_count
    if turtle_sprite_count == 0:
        if turtle_face_turn == 0:
            screen.blit(turtle,(turtle_x,turtle_y),turtle_rect_walk1_left)
        else:
            screen.blit(turtle,(turtle_x,turtle_y),turtle_rect_walk1_right)
    elif turtle_sprite_count == 1:
        if turtle_face_turn == 0:
            screen.blit(turtle,(turtle_x,turtle_y),turtle_rect_walk2_left)
        else:
            screen.blit(turtle,(turtle_x,turtle_y),turtle_rect_walk2_right)

    turtle_sprite_count += 1
    if turtle_sprite_count == 2:
        turtle_sprite_count = 0


def turtle_walk():
    global turtle_walk_count,turtle_x,turtle_face_turn,mario_x

    if abs(turtle_x - mario_x) > 100:
        if turtle_walk_count < 10:
            turtle_x -= 5
            turtle_face_turn = 0
        else:
            turtle_x += 5
            turtle_face_turn = 1

        turtle_walk_count += 1
        if turtle_walk_count >= 20:
            turtle_walk_count = 0
            turtle_face_turn = 0

    else:
        #check direction of mario
        #if mario is left of turtle
        if mario_x < turtle_x:
            turtle_x -= 5
            turtle_face_turn = 0
        else:
            turtle_x += 5
            turtle_face_turn = 1
        turtle_walk_count = 0

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
    global points,mario_alive
    mario = pygame.Rect(mario_x,mario_y,mario_w,mario_h)
    #print(mario)
    for i in range(len(coin_pos)):
        if coin_pos[i] == -1:
            continue
        coin = pygame.Rect( coin_pos[i][0], coin_pos[i][1], 18,18)

        if mario.colliderect(coin):
            coin_effect.play()
            coin_pos[i] = -1
            points += 5

    turtle = pygame.Rect( turtle_x, turtle_y,20,27)
    if mario.colliderect(turtle):
        mario_alive = False

def draw_mario_die():
    global screen,mario_walk_count,is_play_die_sound
    screen.blit(mario,(mario_x,mario_y - 15),mario_die_rect)

    if is_play_die_sound == False:
        pygame.mixer.music.stop()
        mario_die_effect.play()
        is_play_die_sound = True

def draw_mario_jump():
    global screen,mario_face_turn

    if mario_face_turn == 0:
        screen.blit(mario,(mario_x,mario_y),mario_rect_left_jump)
    else:
        screen.blit(mario,(mario_x,mario_y),mario_rect_right_jump)


def mario_jump():
    global mario_x,mario_y,mario_face_turn,mario_vel_x,jump_step,mario_is_jump,is_play_jump_sound

    if mario_is_jump == False:
        return

    if mario_face_turn == 1:
        if mario_vel_x > 4:
            mario_vel_x = 4
        mario_x += mario_vel_x
        #mario_x += 2
        if jump_step < 10:
            mario_y -=  5
        else:
            mario_y +=  5
    elif mario_face_turn == 0:
        if mario_vel_x > 4:
            mario_vel_x = 4
        mario_x -= mario_vel_x
        #mario_x -= 2
        if jump_step < 10:
            mario_y -=  5
        else:
            mario_y +=  5

    jump_step += 1
    if jump_step >= 20:
        jump_step = 0
        mario_is_jump = False
        is_play_jump_sound = False


while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True

        if mario_alive == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:

                    effect.play()
                    mario_walking = True
                    if mario_face_turn != 0:
                        mario_vel_x = 0

                    mario_face_turn = 0

                    #if mario_vel_x > 0:
                        #mario_vel_x = 0

                    mario_vel_x += 2

                elif event.key == pygame.K_RIGHT:

                    effect.play()
                    mario_walking = True
                    if mario_face_turn != 1:
                        mario_vel_x = 0

                    mario_face_turn = 1

                    #if mario_vel_x < 0:
                        #mario_vel_x = 0

                    mario_vel_x += 2
                #if event.key == pygame.K_LEFT and event.key == pygame.K_SPACE and:

                elif event.key == pygame.K_SPACE:
                    mario_is_jump = True
            else:
                mario_walking = False

                mario_vel_x -= 1
                if mario_vel_x <= 0:
                    mario_vel_x = 0


    screen.blit(mario_back,(0,0))

    if mario_alive == True:
        if mario_is_jump == True:
            mario_jump()
            draw_mario_jump()
            if is_play_jump_sound == False:
                mario_jump_effect.play()
                is_play_jump_sound = True

        elif mario_walking == True:
            if mario_face_turn == 0:
                mario_x -= 5
            elif mario_face_turn == 1:
                mario_x += 5
            draw_mario_walk()
        else:
            if mario_face_turn == 0:
                screen.blit(mario,(mario_x,mario_y),mario_rect_left)
            else:
                screen.blit(mario,(mario_x,mario_y),mario_rect_right)

        loop_count += 1
        if loop_count % 10 == 0:
            turtle_walk()

        check_collide()

        draw_turtle_walk()
    else:
        draw_mario_die()

    text = myfont.render("points : " + str(points), True, (255, 0, 0))
    screen.blit(text,  (800 - text.get_width() - 50 , 20))

    text2 = myfont.render("Dev by S Teacher : ", True, (0, 0, 255))
    screen.blit(text2,  (800 - text2.get_width() - 50 , 60))

    draw_coin()
    coin_count += 1

    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM)
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps
