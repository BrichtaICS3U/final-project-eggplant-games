import pygame, random

#Import classes
from hero import Hero, Enemy, Bullet

pygame.init()

def TEXT(TXT,x,y,TF):
    """this function exists to create headings for each menu screens"""

    fontTitle = pygame.font.Font('freesansbold.ttf', TF)
    textSurfaceTitle = fontTitle.render(TXT, True,M_TEXT)
    textRectTitle = textSurfaceTitle.get_rect()
    textRectTitle.center = (x,y)
    screen.blit(textSurfaceTitle,textRectTitle)

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (81, 222, 232)
BLACK = (0, 0, 0)
M_TEXT = (164,44,214)
        
SCREENWIDTH=1250
SCREENHEIGHT=800
 
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Irrelevant")

#List containing all sprites 
all_sprites_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

#Create Hero, enemy
player = Hero(30, 50)
player.rect.x = 200
player.rect.y = 300
playerHealth = player.HP

enemy = Enemy(BLACK, 40, 40)
enemy_list.add(enemy)
 
# Add sprites to list of sprites
all_sprites_list.add(player)
all_sprites_list.add(enemy)

#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()
 
while carryOn:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                carryOn=False
         
        keys = pygame.key.get_pressed()

        #Player Move
        if keys[pygame.K_a]:
            player.move()
        if keys[pygame.K_d]:
            player.move()
        if keys[pygame.K_w]:
            player.move()
        if keys[pygame.K_s]:
           player.move()

        #Player Sprint
        if keys[pygame.K_LSHIFT]:
            if keys[pygame.K_a]:
                player.sprint()
            elif keys[pygame.K_d]:
                player.sprint()
            elif keys[pygame.K_w]:
                player.sprint()
            elif keys[pygame.K_s]:
                player.sprint()
                    
        #Enemy follow player
        enemy.move_to_player(player)
                
        #If enemy hits player
        collision_list = pygame.sprite.spritecollide(player, enemy_list, False)

        #Shooting bullets
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet (from player) if the user clicks the mouse button
            bullet = Bullet(BLACK, 5, 5, player.rect.x, player.rect.y)
            # Add the bullet to the lists
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)
            bullet_collision = pygame.sprite.spritecollide(bullet, enemy_list, False)
            
                        
        #Game Logic
        all_sprites_list.update()
        
        #Drawing on Screen
        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, [20, 30, 15, 25], 0) #Draw player health bars
        pygame.draw.rect(screen, GREEN, [40, 30, 15, 25], 0)
        pygame.draw.rect(screen, GREEN, [60, 30, 15, 25], 0)
        pygame.draw.rect(screen, GREEN, [80, 30, 15, 25], 0)
        pygame.draw.rect(screen, GREEN, [100, 30, 15, 25], 0)
        TEXT("Player Health", 60, 20, 15)

        #Updating health bars
        for collision in collision_list:
            player.HP -= 20

        #while player.HP <= 100:
            #if player.HP == 80:
                #pygame.draw.rect(screen, WHITE, [100, 30, 15, 25], 0)
            #elif player.HP == 60:
                #pygame.draw.rect(screen, WHITE, [80, 30, 15, 25], 0)
            #elif player.HP == 40:
                #pygame.draw.rect(screen, WHITE, [60, 30, 15, 25], 0)
            #elif player.HP == 20:
                #pygame.draw.rect(screen, WHITE, [40, 30, 15, 25], 0)
            #elif player.HP == 0:
                #pygame.draw.rect(screen, WHITE, [20, 30, 15, 25], 0)
                #player.die()
        
        #Draw all the sprites
        all_sprites_list.draw(screen)
 
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pygame.quit()
