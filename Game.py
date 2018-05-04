import pygame
pygame.init()

from Button import BUTTON

WHITE = (255,255,255)
GRAY  = (121,121,121)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)



SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 800
size = (SCREEN_WIDTH,SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

Game = True
menu = 'Start'
clock = pygame.time.Clock()



button1 = BUTTON("hey",SCREEN_WIDTH/2,SCREEN_HEIGHT/2,RED,BLUE)
while Game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
        elif event.type == pygame.KEYDOWN:
            if event.key==pygame.K_x:
                Game = False


# ------ Draw code for menu will go here -------- #
    screen.fill(WHITE)

    #title 
    fontTitle = pygame.font.Font('freesansbold.ttf', 70)
    textSurfaceTitle = fontTitle.render('Ctrl and Destroy', True,BLACK)
    textRectTitle = textSurfaceTitle.get_rect()
    textRectTitle.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/5)

    screen.blit(textSurfaceTitle,textRectTitle)
    button1.draw()

    
    
    










    
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()

