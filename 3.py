import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
mario = pygame.image.load('mario.gif')
mario_back = pygame.image.load('mario_back.png')

r1 = pygame.Rect(11,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด
done = False
clock = pygame.time.Clock()   #ตัวกำหนด frame rate

while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True

    screen.blit(mario_back,(0,0))
    screen.blit(mario,(65,533),r1)

    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM)
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps
