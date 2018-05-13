import pygame

BLACK = (0,0,0)

class HOLE(pygame.sprite.Sprite):


    def __init__(self,width,height,colour=BLACK):

        self.width = width
        slf.height = height
        self.colour = colour

        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image,BLACK,[0,0,width,height])

        self.rect = self.image.get_rect()
