import pygame
from hero import Hero

WHITE = (255,255,255)
BLACK = (0,0,0)

class DOOR(pygame.sprite.Sprite):

    def __init__(self,width,height,colour = BLACK):
        super().__init__()
        
        self.colour = colour
        self.height = height
        self.width = width

        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image,self.colour,[0,0,width,height])

        self.rect = self.image.get_rect()


        #def Lock(self,colour):



class KEY(pygame.sprite.Sprite):

    def __init__(self,width,height,colour = BLACK):
        super().__init__()

        self.width = width
        self.height = height
        self.colour = colour

        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image,self.colour,[0,0,width,height])

        self.rect = self.image.get_rect()
