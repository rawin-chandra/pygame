import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
mario = pygame.image.load('mario.gif')
mario_back = pygame.image.load('mario_back.png')

effect = pygame.mixer.Sound('mario_sound.wav')

pygame.mixer.music.load('stage1.mp3')
pygame.mixer.music.play(-1)

mario.set_colorkey((255,255,255))
mario_x = 65
mario_y = 533
r1 = pygame.Rect(11,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด
done = False
clock = pygame.time.Clock()   #ตัวกำหนด frame rate

while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mario_x -= 10
                effect.play()
            if event.key == pygame.K_RIGHT:
                mario_x += 10
                effect.play()

    screen.blit(mario_back,(0,0))
    screen.blit(mario,(mario_x,mario_y),r1)

    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM)
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps
