import pygame
from hero import Hero

WHITE = (255,255,255)
BLACK = (0,0,0)



class DOOR(pygame.sprite.Sprite):

    def __init__(self,width,height,colour = BLACK, LOCK = 0, OPEN = False):
        super().__init__()
        
        self.colour = colour
        self.height = height
        self.width = width
        self.LOCK  = LOCK
        self.OPEN  = OPEN

        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image,self.colour,[0,0,width,height])

        self.rect = self.image.get_rect()


        #def Lock(self,colour):

    def IS_LOCKED(self):
            self.OPEN = True

class KEY(pygame.sprite.Sprite):

    def __init__(self,width,height,colour = BLACK, D_N = 0):
        super().__init__()

        self.width = width
        self.height = height
        self.colour = colour
        self.D_N    = D_N

        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image,self.colour,[0,0,width,height])

        self.rect = self.image.get_rect()

    
        
        
