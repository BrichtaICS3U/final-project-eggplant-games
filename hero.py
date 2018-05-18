import pygame, random, math

BLUE = (125, 215, 245)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
class Hero(pygame.sprite.Sprite):
    #Hero/main character class that derives from pygame "Sprite" class.
    
    def __init__(self, width, height, HP=100):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.HP = HP
        
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

    def sprint(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]: #Up 
            self.rect.y -= 2
        if keys[pygame.K_s]: #Down
           self.rect.y += 2
        if keys[pygame.K_a]: #Left
            self.rect.x -= 2
        if keys[pygame.K_d]: #Right
            self.rect.x += 2

    def die(self):
        print("You died!")

    def health(self,screen):
        if self.HP <= 80:
            pygame.draw.rect(screen, WHITE, [100, 30, 15, 25], 0)
            if self.HP <= 60:
                pygame.draw.rect(screen, WHITE, [80, 30, 15, 25], 0)
                if self.HP <= 40:
                    pygame.draw.rect(screen, WHITE, [60, 30, 15, 25], 0)
                if self.HP <= 20:
                    pygame.draw.rect(screen, WHITE, [40, 30, 15, 25], 0)
                if self.HP == 0:
                    pygame.draw.rect(screen, WHITE, [20, 30, 15, 25], 0)
                    self.die()
                    carryOn = False
                    pygame.quit()

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, colour, width, height, x_pos, y_pos, speed=2):
        super().__init__()
        self.speed = speed
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, BLACK, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # find vector between bullet and mouse
        self.dist_x = self.rect.x - mouse_x
        self.dist_y = self.rect.y - mouse_y
        
        # get diagonal line between bullet and mouse
        distance = math.hypot(self.dist_x, self.dist_y)
        self.dist_x, self.dist_y = self.dist_x / distance, self.dist_y / distance
    
    def update(self):      
        # move along vector towards the mouse click 
        self.rect.x -= self.dist_x * 3
        self.rect.y -= self.dist_y * 3
        
        
class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, colour, width, height, HP=100, dmg=10):
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
        # find direction vector between enemy and player
        dist_x = self.rect.x - player.rect.x
        dist_y = self.rect.y - player.rect.y
        
        # get diagonal line between enemy and player
        distance = math.hypot(dist_x, dist_y)
        dist_x, dist_y = dist_x / distance, dist_y / distance
        
        # move along vector towards the player at current speed
        speed = 2
        self.rect.x -= dist_x * speed
        self.rect.y -= dist_y * speed

        #https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame

    def die(self):
        print("Enemy died!")

    def health(self, screen):
        if self.HP <= 80:
                pygame.draw.rect(screen, WHITE, [self.rect.x+29, self.rect.y-10, 6, 5], 0)
                if self.HP <= 60:
                    pygame.draw.rect(screen, WHITE, [self.rect.x+23, self.rect.y-10, 6, 5], 0)
                    if self.HP <= 40:
                        pygame.draw.rect(screen, WHITE, [self.rect.x+17, self.rect.y-10, 6, 5], 0)
                        if self.HP <= 20:
                            pygame.draw.rect(screen, WHITE, [self.rect.x+11, self.rect.y-10, 6, 5], 0)
                            
    
         

        



        


     
        
        
        
        
        
        
        


