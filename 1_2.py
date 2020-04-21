import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800,600))

done = False
screen.fill((0,0,255))
x = 100
while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    pygame.draw.rect(screen,(255,0,0),(x,100,200,100),5)
    pygame.display.update()

    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True

    x = x + 10
    time.sleep(1)
