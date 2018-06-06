import pygame, random, math

BLUE = (125, 215, 245)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0,255,0)
GREY = (100, 100, 100)
RED = (255, 0, 0)
ORANGE = (247,163,7)

 
class Hero(pygame.sprite.Sprite):
    #Hero/main character class that derives from pygame "Sprite" class.
    
    def __init__(self, width, height, HP=100, ammo=5, money=0, movespeed=4):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.HP = HP
        self.ammo = ammo
        self.money = money
        self.movespeed = movespeed
        
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
            self.rect.y -= self.movespeed
        if keys[pygame.K_s]:# Down
           self.rect.y += self.movespeed
        if keys[pygame.K_a]: #Left
            self.rect.x -= self.movespeed
        if keys[pygame.K_d]: #Right
            self.rect.x += self.movespeed


    def sprint(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]: #Up 
            self.rect.y -= self.movespeed -3
        if keys[pygame.K_s]: #Down
           self.rect.y += self.movespeed -3
        if keys[pygame.K_a]: #Left
            self.rect.x -= self.movespeed -3
        if keys[pygame.K_d]: #Right
            self.rect.x += self.movespeed -3
        
    def die(self):
        print("You died!")

class Sword(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos, width, height):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        pygame.draw.rect(self.image, GREY, [0, 0, width, height])
        
        self.rect = self.image.get_rect()

    def up(self, player, screen):
      
        self.width = 5
        self.height = 25
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x+12.5
        self.rect.y = player.rect.y-25
        
    def down(self, player, screen):
        self.width = 5
        self.height = 25
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x+12.5
        self.rect.y = player.rect.y+40
        
    def right(self, player, screen):
        self.width = 25
        self.height = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x+30
        self.rect.y = player.rect.y+17.5
        
    def left(self, player, screen):       
        self.width = 25
        self.height = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x+-25
        self.rect.y = player.rect.y+17.5

    def draw(self, player, screen):
        pygame.draw.rect(self.image, GREY, [0, 0, self.width, self.height])
        screen.blit(self.image, (player.rect.x, player.rect.y))
        
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, colour, width, height, x_pos, y_pos):
        super().__init__()
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
        # move along vector towards the mouse click at speed of 3 pixels
        self.rect.x -= self.dist_x * 5
        self.rect.y -= self.dist_y * 5        
        
        
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
        speed = 7
        self.rect.x -= dist_x * speed
        self.rect.y -= dist_y * speed

        #https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame

    def die(self):
        print("Enemy died!")

    def health(self, screen):
        if self.HP >= 10:
            pygame.draw.rect(screen, RED, [self.rect.x+5, self.rect.y-10, 3, 5], 0)
            if self.HP >= 20:
                pygame.draw.rect(screen, RED, [self.rect.x+8, self.rect.y-10, 3, 5], 0)
                if self.HP >= 30:
                    pygame.draw.rect(screen, RED, [self.rect.x+11, self.rect.y-10, 3, 5], 0)
                    if self.HP >= 40:
                        pygame.draw.rect(screen, RED, [self.rect.x+14, self.rect.y-10, 3, 5], 0)
                        if self.HP >= 50:
                            pygame.draw.rect(screen, RED, [self.rect.x+17, self.rect.y-10, 3, 5], 0)
                            if self.HP >= 60:
                                pygame.draw.rect(screen, RED, [self.rect.x+20, self.rect.y-10, 3, 5], 0)
                                if self.HP >= 70:
                                    pygame.draw.rect(screen, RED, [self.rect.x+23, self.rect.y-10, 3, 5], 0)
                                    if self.HP >= 80:
                                        pygame.draw.rect(screen, RED, [self.rect.x+26, self.rect.y-10, 3, 5], 0)
                                        if self.HP >= 90:
                                            pygame.draw.rect(screen, RED, [self.rect.x+29, self.rect.y-10, 3, 5], 0)
                                            if self.HP == 100:
                                                pygame.draw.rect(screen, RED, [self.rect.x+32, self.rect.y-10, 3, 5], 0)

class Drops(pygame.sprite.Sprite):

    def __init__(self, colour, width, height, x_pos, y_pos):
        super().__init__()
        self.colour = colour
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, colour, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

class StorePlate(pygame.sprite.Sprite):

    def __init__(self, colour, x_pos, y_pos, width, height):
        super().__init__()
        self.colour = colour
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, colour, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def drawExtra(self, screen):
        pygame.draw.rect(screen, BLACK, [(154)+58.5, (800-300)+38.5, 5, 5], 0)              #single bullet
        pygame.draw.rect(screen, BLACK, [(428)+(120/4)-2.5, (800-300)+38.5, 5, 5], 0)       #3 bullets
        pygame.draw.rect(screen, BLACK, [(428)+(120/4*2)-2.5, (800-300)+38.5, 5, 5], 0)     #
        pygame.draw.rect(screen, BLACK, [(428)+(120/4*3)-2.5, (800-300)+38.5, 5, 5], 0)     #
        pygame.draw.rect(screen, GREEN, [(702)+52.5, (800-300)+27.5, 15, 25], 0)             #health bar
        pygame.draw.line(screen, ORANGE,((976)+35, 800-275), ((976)+50,(800-260)), 5)       #speed boost lines
        pygame.draw.line(screen, ORANGE,((976)+50, 800-260), ((976)+35,800-245), 5)
        pygame.draw.line(screen, ORANGE,((976)+55, 800-275), ((976)+70,(800-260)), 5)
        pygame.draw.line(screen, ORANGE,((976)+70, 800-260), ((976)+55,800-245), 5)
        pygame.draw.line(screen, ORANGE,((976)+75, 800-275), ((976)+90,(800-260)), 5)
        pygame.draw.line(screen, ORANGE,((976)+90, 800-260), ((976)+75,800-245), 5)

    
                                 
class HealthBar():

    def __init__(self, screen, player):

        if player.HP == 0:
            player.die()
            pygame.quit()

        elif player.HP >= 10:
            pygame.draw.rect(screen, GREEN, [20, 30, 15, 12.5], 0)
            if player.HP >= 20:
                pygame.draw.rect(screen, GREEN, [20, 42.5, 15, 12.5], 0)
                if player.HP >= 30:
                    pygame.draw.rect(screen, GREEN, [40, 30, 15, 12.5], 0)
                    if player.HP >= 40:
                        pygame.draw.rect(screen, GREEN, [40, 42.5, 15, 12.5], 0)
                        if player.HP >= 50:
                            pygame.draw.rect(screen, GREEN, [60, 30, 15, 12.5], 0)
                            if player.HP >= 60:
                                pygame.draw.rect(screen, GREEN, [60, 42.5, 15, 12.5], 0)
                                if player.HP >= 70:
                                    pygame.draw.rect(screen, GREEN, [80, 30, 15, 12.5], 0)
                                    if player.HP >= 80:
                                        pygame.draw.rect(screen, GREEN, [80, 42.5, 15, 12.5], 0)
                                        if player.HP >= 90:
                                            pygame.draw.rect(screen, GREEN, [100, 30, 15, 12.5], 0)
                                            if player.HP == 100:
                                                pygame.draw.rect(screen, GREEN, [100, 42.5, 15, 12.5], 0)

class AmmoBar():

    def __init__(self, screen, player):

        if player.ammo > 0:
            pygame.draw.ellipse(screen, BLACK, [20, 90, 15, 25], 0) #draws player ammo
            if player.ammo > 1:
                pygame.draw.ellipse(screen, BLACK, [40, 90, 15, 25], 0)
                if player.ammo > 2:
                    pygame.draw.ellipse(screen, BLACK, [60, 90, 15, 25], 0)
                    if player.ammo > 3:
                        pygame.draw.ellipse(screen, BLACK, [80, 90, 15, 25], 0)
                        if player.ammo > 4:
                            pygame.draw.ellipse(screen, BLACK, [100, 90, 15, 25], 0)


        


    

    

        
      
         

        



        


     
        
        
        
        
        
        
        


