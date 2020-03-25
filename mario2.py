import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

mario = pygame.image.load('mario.gif')
mario_back = pygame.image.load('mario_back.png')

mario.set_colorkey((255,255,255))

pygame.mixer.music.load('stage1.mp3')
pygame.mixer.music.play(-1)

r = pygame.Rect(248,1,30,20)
mario_x = 30
mario_y = 535

done = False
while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                mario_x -= 10
            if event.key == pygame.K_RIGHT:
                mario_x += 10
    screen.blit(mario_back,(0,0))
    screen.blit(mario,(mario_x,mario_y),r)

    pygame.display.flip()
