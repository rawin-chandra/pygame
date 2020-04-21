import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
mario = pygame.image.load('mario.gif')
mario_back = pygame.image.load('mario_back.png')
effect = pygame.mixer.Sound('mario_sound.wav')
pygame.mixer.music.load('stage1.mp3')
pygame.mixer.music.play(-1)
mario.set_colorkey((255,255,255))
mario_x = 400 #65
mario_y = 535
mario_rect_right = pygame.Rect(11,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด
mario_rect_left = pygame.Rect(30,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด

mario_rect_walk1_left = pygame.Rect(138,4,20,20)
mario_rect_walk2_left = pygame.Rect(211,4,20,20)
mario_rect_walk1_right = pygame.Rect(114,4,20,20)
mario_rect_walk2_right = pygame.Rect(186,4,20,20)

mario_walking = False
mario_face_turn = 1  # 0 = left, 1 = right
done = False
clock = pygame.time.Clock()   #ตัวกำหนด frame rate

mario_walk_count = 0
def mario_walk():
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

    screen.blit(mario_back,(0,0))
    if mario_walking == True:
        mario_walk()
    else:
        if mario_face_turn == 0:
            screen.blit(mario,(mario_x,mario_y),mario_rect_left)
        else:
            screen.blit(mario,(mario_x,mario_y),mario_rect_right)

    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM)
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps
