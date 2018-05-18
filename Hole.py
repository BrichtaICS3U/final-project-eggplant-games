import pygame

<<<<<<< HEAD
=======
WHITE = (255,255,255)
>>>>>>> master
BLACK = (0,0,0)

class HOLE(pygame.sprite.Sprite):


    def __init__(self,width,height,colour=BLACK):
<<<<<<< HEAD

        self.width = width
        slf.height = height
=======
        super().__init__()

        self.width = width
        self.height = height
>>>>>>> master
        self.colour = colour

        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image,BLACK,[0,0,width,height])

        self.rect = self.image.get_rect()
<<<<<<< HEAD
=======

        
>>>>>>> master
