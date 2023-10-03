import pygame

pygame.init()


#creates game screen and caption
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Pong")

#game variables
doExit = False #variable to quit out of game loop

clock = pygame.time.Clock()

p1x = 20
p1y = 200

p1Score = 0
p2Score = 0

p2x = 650
p2y = 200

bx = 350
by = 250

bVx = 5
bVy = 5

#BEGIN GAME LOOP######################################################
while not doExit:

    clock.tick(60)
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1y-=5
    if keys[pygame.K_s]:
        p1y+=5
    
    keys2 = pygame.key.get_pressed()
    if keys2[pygame.K_UP]:
        p2y-=5
    if keys2[pygame.K_DOWN]:
        p2y+=5

    bx += bVx
    by += bVy

    if by <= 0 or by + 20 >= 500:
       bVy *= -1
    
    #left paddle collision
    if bx-20 < p1x + 20 and by + 20 > p1y and by < p1y + 100:
        bVx *= -1
        
    #right paddle collision
    if by < p2y + 100 and bx + 20 > p2x and by + 20 > p2y:
        bVx *= -1

    if bx < 10:
        bVx *= -1
        p2Score += 1
        
    elif bx > 680:
        bVx *= -1
        p1Score += 1
        
    
    

    #render section-----------------------------------
    screen.fill((0,0,0)) #wipe the screen black
    
    screen.fill((0,0,0))

    font = pygame.font.Font(None, 74)

    text = font.render(str(p1Score), 1, (255,255,255))

    screen.blit(text, (250,10))

    text = font.render(str(p2Score), 1, (255,255,255))

    screen.blit(text, (420,10))

    pygame.draw.line(screen, (255,255,255), [349, 0], [349, 500], 5)

    pygame.draw.rect(screen, (255,255,255), (p1x, p1y, 20, 100), 20)

    pygame.draw.rect(screen, (255,255,255), (p2x, p2y, 20, 100), 20)

    pygame.draw.circle(screen, (255, 255, 255), (bx, by), 15)

    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()
