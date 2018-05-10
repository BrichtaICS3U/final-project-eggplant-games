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

        pygame.draw.rect(self.image,BLACK,[0,0,width,height])

        self.rect = self.image.get_rect()



    def NEXT_SCREEN_UP(self):
        """this function will transfer the player to a new screen UP and reset their position in the correct area"""
        player.rect.y = SCREEN_HEIGHT - 46

    def NEXT_SCREEN_RIGHT(self):
        """this function will transfer the player to a new screen RIGHT and reset their position in the correct area"""
        player.rect.x = 6

    def NEXT_SCREEN_LEFT(self):
        """this function will transfer the player to a new screen LEFT and reset their position in the correct area"""
        player.rect.x = SCREEN_WIDTH - 36

    def NEXT_SCREEN_DOWN(self):
        """this function will transfer the player to a new screen UP and reset their position in the correct area"""
        player.rect.y = 6
