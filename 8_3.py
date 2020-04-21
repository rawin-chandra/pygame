import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
mario = pygame.image.load('mario.gif')
turtle = pygame.image.load('enemies.gif')
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
mario.set_colorkey((255,255,255))
turtle.set_colorkey((255,255,255))

font = pygame.font.SysFont("comicsansms", 72)
mario_x = 200 #100 #65
mario_y = 535
mario_w = 14
mario_h = 14

turtle_x = 700 #600 #65
turtle_y = 525

mario_rect_right = pygame.Rect(11,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด
mario_rect_left = pygame.Rect(30,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด
mario_rect_walk1_left = pygame.Rect(138,4,20,20)
mario_rect_walk2_left = pygame.Rect(211,4,20,20)
mario_rect_walk1_right = pygame.Rect(114,4,20,20)
mario_rect_walk2_right = pygame.Rect(186,4,20,20)

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

mario_rect_right_jump = pygame.Rect(48,3,20,20)
mario_rect_left_jump = pygame.Rect(71,3,20,20)

mario_rect_right_jump_big = pygame.Rect(69,26,18,29)
mario_rect_left_jump_big = pygame.Rect(92,176,18,29)

mario_die_rect = pygame.Rect(339,263,18,20)

mushroom_block_rect = pygame.Rect(440, 361, 60, 60);  #440, 361, 46, 46);   443, 256, 18, 18
mushroom_rect = pygame.Rect( 443, 256, 18, 18);

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
mario_is_fall = False
mario_is_big = False

turtle_alive = True

have_mushroom = False
mushroom_x = 443
mushroom_y = 360

screen_x = 0

def draw_mario_walk():
    global screen,mario_walk_count,mario_is_big
    if mario_walk_count == 0:
        if mario_face_turn == 0:
            if mario_is_big == False:
                screen.blit(mario,(mario_x,mario_y),mario_rect_walk1_left)
            else:
                screen.blit(mario,(mario_x,mario_y),mario_rect_walk1_left_big)
        else:
            if mario_is_big == False:
                screen.blit(mario,(mario_x,mario_y),mario_rect_walk1_right)
            else:
                screen.blit(mario,(mario_x,mario_y),mario_rect_walk1_right_big)
    elif mario_walk_count == 1:
        if mario_face_turn == 0:
            if mario_is_big == False:
                screen.blit(mario,(mario_x,mario_y),mario_rect_walk2_left)
            else:
                screen.blit(mario,(mario_x,mario_y),mario_rect_walk2_left_big)
        else:
            if mario_is_big == False:
                screen.blit(mario,(mario_x,mario_y),mario_rect_walk2_right)
            else:
                screen.blit(mario,(mario_x,mario_y),mario_rect_walk2_right_big)
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

def draw_turtle_die():
    global screen
    screen.blit(turtle,(turtle_x,turtle_y + 7),turtle_die_rect)

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
    global points,mario_alive,turtle_alive,mario_face_turn,turtle_x,turtle_y,mario_x,mario_y
    global mushroom_block_rect,have_mushroom,mushroom_x,mushroom_y,mario_is_big,is_mario_effect

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

    if turtle_alive == True:
        turtle = pygame.Rect( turtle_x, turtle_y,20,27)
        if mario.colliderect(turtle):
            if mario_is_fall == True:
                turtle_alive = False
            else:
                mario_alive = False
    else :
        turtle = pygame.Rect( turtle_x, turtle_y,20,27)
        if mario.colliderect(turtle):
            if mario_face_turn == 0:
                turtle_x = mario_x - 8
                turtle_y = mario_y - 5
            else:
                turtle_x = mario_x + 8
                turtle_y = mario_y - 5

    if mario.colliderect(mushroom_block_rect):
        have_mushroom = True
        mushroom_appear_effect.play()

    if have_mushroom == True:
        mush = pygame.Rect(mushroom_x,mushroom_y,18,18)
        if mario.colliderect(mush):
            power_up_effect.play()
            mario_is_big = True
            mario_y = 523
            have_mushroom = False
            is_mario_effect = True


def draw_mario_die():
    global screen,mario_walk_count,is_play_die_sound
    screen.blit(mario,(mario_x,mario_y - 15),mario_die_rect)

    if is_play_die_sound == False:
        pygame.mixer.music.stop()
        mario_die_effect.play()
        is_play_die_sound = True

def draw_mario_jump():
    global screen,mario_face_turn,mario_is_big,mario_x,screen_x,mario_vel_x

    if mario_face_turn == 0:
        if mario_x - screen_x < 400:  # or  mario_x < (screen_x + 400) / 2 :
            screen_x -= mario_vel_x
        if mario_is_big == False:
            screen.blit(mario,(mario_x,mario_y),mario_rect_left_jump)
        else:
            screen.blit(mario,(mario_x,mario_y),mario_rect_left_jump_big)
    else:
        if mario_x - screen_x > 400:
            screen_x += mario_vel_x
        if mario_is_big == False:
            screen.blit(mario,(mario_x,mario_y),mario_rect_right_jump)
        else:
            screen.blit(mario,(mario_x,mario_y),mario_rect_right_jump_big)


def draw_mushroom():
    global screen,mushroom_x,mushroom_y,mushroom_rect

    if mushroom_x > 421 and mushroom_x < 528:
        mushroom_x += 1
        mushroom_y = 345
    elif mushroom_y < 532:   #520:   #550     540
        mushroom_y += 5
        mushroom_x += 1
    else:
        mushroom_y = 532    #515   525
        mushroom_x += 1

    screen.blit(mario,(mushroom_x,mushroom_y),mushroom_rect)

def draw_background():
    global scree,mario_x,screen_x,mario_back

    stage_rect = pygame.Rect(screen_x,0,800,600)
    screen.blit(mario_back,(0,0),stage_rect)

def mario_jump():
    global mario_x,mario_y,mario_face_turn,mario_vel_x,jump_step,mario_is_jump,is_play_jump_sound,mario_is_fall

    if mario_is_jump == False:
        return

    if mario_face_turn == 1:
        if mario_vel_x > 4:
            mario_vel_x = 4
        mario_x += mario_vel_x
        #mario_x += 2
        if jump_step < 10:
            mario_y -=  12
        else:
            mario_y +=  12
            mario_is_fall = True
    elif mario_face_turn == 0:
        if mario_vel_x > 4:
            mario_vel_x = 4
        mario_x -= mario_vel_x
        #mario_x -= 2
        if jump_step < 10:
            mario_y -=  12
        else:
            mario_y +=  12
            mario_is_fall = True

    jump_step += 1
    if jump_step >= 20:
        jump_step = 0
        mario_is_jump = False
        is_play_jump_sound = False
        mario_is_fall = False


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
                    mario_vel_x += 2

                elif event.key == pygame.K_RIGHT:

                    effect.play()
                    mario_walking = True
                    if mario_face_turn != 1:
                        mario_vel_x = 0

                    mario_face_turn = 1
                    mario_vel_x += 2
                #if event.key == pygame.K_LEFT and event.key == pygame.K_SPACE and:

                elif event.key == pygame.K_SPACE:
                    mario_is_jump = True
            else:
                mario_walking = False

                mario_vel_x -= 1
                if mario_vel_x <= 0:
                    mario_vel_x = 0


    if mario_alive == True:
        if mario_is_jump == True:
            mario_jump()
            draw_background()
            draw_mario_jump()
            if is_play_jump_sound == False:
                mario_jump_effect.play()
                is_play_jump_sound = True

        elif mario_walking == True:
            if mario_face_turn == 0:
                mario_x -= 5
                if mario_x - screen_x < 400:  # or  mario_x < (screen_x + 400) / 2 :
                    screen_x -= 5
            elif mario_face_turn == 1:
                mario_x += 5
                if mario_x - screen_x > 400:  # and mario_x > (screen_x + 400) / 2 :
                    screen_x += 5
            draw_background()
            draw_mario_walk()
        else:
            draw_background()
            if mario_face_turn == 0:
                if mario_is_big == False:
                    screen.blit(mario,(mario_x,mario_y),mario_rect_left)
                else:
                    screen.blit(mario,(mario_x,mario_y),mario_rect_left_big)
            else:
                if mario_is_big == False:
                    screen.blit(mario,(mario_x,mario_y),mario_rect_right)
                else:
                    screen.blit(mario,(mario_x,mario_y),mario_rect_right_big)

        if turtle_alive == True:
            loop_count += 1
            if loop_count % 10 == 0:
                turtle_walk()

            draw_turtle_walk()

        else:
            draw_turtle_die()

        check_collide()


    else:
        draw_mario_die()

    text = myfont.render("points : " + str(points), True, (255, 0, 0))
    screen.blit(text,  (800 - text.get_width() - 50 , 20))

    text2 = myfont.render("Dev by S Teacher : ", True, (0, 0, 255))
    screen.blit(text2,  (800 - text2.get_width() - 50 , 60))

    if have_mushroom:
        draw_mushroom()

    draw_coin()
    coin_count += 1


    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM)
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps
