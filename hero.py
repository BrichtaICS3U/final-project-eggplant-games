import pygame, random, math

BLUE = (125, 215, 245)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
class Hero(pygame.sprite.Sprite):
    #Hero/main character class that derives from pygame "Sprite" class.
    
    def __init__(self, width, height, health=100):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.health = health
        
        # Pass in the color of the hero, x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        # Draw the hero
        pygame.draw.rect(self.image, BLUE, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]: #Up
            self.rect.y -= 2
        if keys[pygame.K_s]:# Down
           self.rect.y += 2
        if keys[pygame.K_a]: #Left
            self.rect.x -= 2
        if keys[pygame.K_d]: #Right
            self.rect.x += 2

        #Fix auto sprint when 2 keys are pressed

    def sprint(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]: #Up 
            self.rect.y -= 2
        if keys[pygame.K_s]:# Down
           self.rect.y += 2
        if keys[pygame.K_a]: #Left
            self.rect.x -= 2
        if keys[pygame.K_d]: #Right
            self.rect.x += 2

    def die(self):
        #Add in health bar diminishing, screen pop up saying player died, etc
        health = 0
        print("You died!")

class Enemy(pygame.sprite.Sprite):
    #Enemy class that derives from pygame "Sprite" class.
    
    def __init__(self, colour, width, height, HP=100, dmg=10):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.colour = colour
        self.HP = HP
        self.dmg = dmg

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, BLACK, [0, 0, width, height])
        self.rect = self.image.get_rect()

        # Get random x/y coordinates
        self.rect.x = random.randrange(0, 1250)
        self.rect.y = random.randrange(0, 800)

    def move_to_player(self, player):
        #https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame
        # find direction vector between enemy and player
        dist_x = self.rect.x - player.rect.x
        dist_y = self.rect.y - player.rect.y
        # get diagonal line between enemy and player
        distance = math.hypot(dist_x, dist_y)
        dist_x, dist_y = dist_x / distance, dist_y / distance
        # move along vector towards the player at current speed
        self.rect.x -= dist_x * 3
        self.rect.y -= dist_y * 3

        



        


     
        
        
        
        
        
        
        


