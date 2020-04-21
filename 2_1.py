import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))

mario = pygame.image.load('mario.gif')


done = False
r1 = pygame.Rect(11,4,14,17)   #สี่เหลี่่ยมของภาพมาริโอ ตอนหยุด

clock = pygame.time.Clock()   #ตัวกำหนด frame rate


while not done:   #game loop  (ให้ใช้เวลาน้อยสุด)
    for event in pygame.event.get(): #เช็คอินพุท
        if event.type == pygame.QUIT:  #ออกโปรแกรม
            done = True

    screen.blit(mario,(100,100),r1) #วาดรูปจาก mario surface ไปที่ตำแหน่ง 50,100 โดยใช้ภาพมาริโอจาก r1

    pygame.display.flip()    #วาดลงการ์ดจอ (ก่อนหน้านี้ วาดใน RAM)
    clock.tick(30);          #ปรับเวลาให้ตรง 30 fps

    
