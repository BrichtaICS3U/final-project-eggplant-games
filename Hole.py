import pygame


WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE  =  (0,0,255)
WT = pygame.image.load("TEST_WALL.png")
BX = 0
BY = 0

class HOLE(pygame.sprite.Sprite):


    def __init__(self,width,height,colour=BLACK):

        super().__init__()

        self.width = width
        self.height = height
        self.colour = colour

        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image,WHITE,[0,0,width,height])

        self.rect = self.image.get_rect()



    def Draw_test(self):
        global BX
        global BY
        
        for i in range (2):
            self.image.blit(WT,[BX,BY])
            BX += 50
