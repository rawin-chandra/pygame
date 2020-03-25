import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

mario = pygame.image.load('mario.gif')
mario_back = pygame.image.load('mario_back.png')

mario_stuff = pygame.image.load('mario_stuff.png')

mario.set_colorkey((255,255,255))
mario_stuff.set_colorkey((0,0,0))

pygame.mixer.music.load('stage1.mp3')
pygame.mixer.music.play(-1)

r = pygame.Rect(11,5,16,17)
mario_x = 30
mario_y = 535

t = pygame.Rect(71,330,19,21)
t_x = 500
t_y = 535
count = 0
done = False
turtle_walk_step = 0
turtle_dir = True

clock = pygame.time.Clock() 
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


    pygame.display.flip()
    clock.tick(30); 
